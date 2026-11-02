/**
 * CSI — Forwarded Thread Capture
 *
 * Saves Gmail threads you label into a Google Drive folder as plain text, so the
 * CSI agent team can read them. Solves the "set up a mailbox I can forward to"
 * problem without a mailbox: you forward or label a thread, this picks it up.
 *
 * HOW TO INSTALL (about five minutes, once)
 *
 *  1. Create a Drive folder named exactly:  CSI — Forwarded Threads
 *     (or change FOLDER_NAME below to whatever you call it)
 *
 *  2. Go to https://script.google.com and click "New project".
 *     Name it "CSI Thread Capture".
 *
 *  3. Delete the sample code, paste this whole file in, and Save.
 *
 *  4. In Gmail, create a label named exactly:  CSI-Agent
 *     (Settings → Labels → Create new label)
 *
 *  5. Back in Apps Script, click "Run" and pick `captureThreads`.
 *     Google will ask you to authorize it — approve the Gmail and Drive scopes.
 *     You will see an "unverified app" warning because it is your own script:
 *     click Advanced → "Go to CSI Thread Capture (unsafe)". It is your code.
 *
 *  6. Click the clock icon ("Triggers") in the left sidebar → "Add Trigger".
 *     Function: captureThreads
 *     Event source: Time-driven
 *     Type: Hour timer → Every hour
 *     Save.
 *
 * HOW TO USE IT
 *
 *   Apply the "CSI-Agent" label to any Gmail thread. Within the hour it lands in
 *   the Drive folder as a .txt file and the label is swapped for "CSI-Agent-Saved"
 *   so it is not captured twice. Forwarding to yourself and labelling works too.
 *
 *   To pull something immediately, open the script and click Run.
 *
 * WHAT IT DELIBERATELY DOES NOT DO
 *
 *   - It does not read your whole mailbox. Only threads you explicitly label.
 *   - It does not delete or modify your email beyond swapping that one label.
 *   - It does not send anything.
 *
 * PRIVACY NOTE (CLAUDE.md §7.2)
 *
 *   Threads you label land in a repo-adjacent workflow and are read by agents.
 *   Do not label threads containing decedent names, family contact details, or
 *   death certificate contents. Business correspondence only.
 */

const FOLDER_NAME = 'CSI — Forwarded Threads';
const LABEL_PENDING = 'CSI-Agent';
const LABEL_DONE = 'CSI-Agent-Saved';
const MAX_THREADS_PER_RUN = 25;
const MAX_BODY_CHARS = 100000;

/**
 * Entry point. Finds labelled threads, writes each to Drive, re-labels it.
 */
function captureThreads() {
  const pending = GmailApp.getUserLabelByName(LABEL_PENDING);
  if (!pending) {
    throw new Error(
      'Gmail label "' + LABEL_PENDING + '" not found. Create it in Gmail first.'
    );
  }
  const done = getOrCreateLabel_(LABEL_DONE);
  const folder = getOrCreateFolder_(FOLDER_NAME);

  const threads = pending.getThreads(0, MAX_THREADS_PER_RUN);
  if (threads.length === 0) {
    console.log('Nothing labelled ' + LABEL_PENDING + '. Done.');
    return;
  }

  let saved = 0;
  threads.forEach(function (thread) {
    try {
      const name = buildFileName_(thread);
      folder.createFile(name, renderThread_(thread), MimeType.PLAIN_TEXT);
      thread.addLabel(done);
      thread.removeLabel(pending);
      saved += 1;
      console.log('Saved: ' + name);
    } catch (err) {
      // Leave the label on so the next run retries this thread.
      console.error(
        'Failed on "' + thread.getFirstMessageSubject() + '": ' + err.message
      );
    }
  });

  console.log('Saved ' + saved + ' of ' + threads.length + ' thread(s) to ' + FOLDER_NAME);
}

/**
 * Renders a thread as readable plain text: header block, then each message.
 */
function renderThread_(thread) {
  const messages = thread.getMessages();
  const lines = [
    '=========================================================',
    'SUBJECT: ' + thread.getFirstMessageSubject(),
    'MESSAGES: ' + messages.length,
    'LAST ACTIVITY: ' + thread.getLastMessageDate().toISOString(),
    'CAPTURED: ' + new Date().toISOString(),
    'GMAIL LINK: ' + thread.getPermalink(),
    '=========================================================',
    '',
  ];

  messages.forEach(function (msg, i) {
    lines.push('--- MESSAGE ' + (i + 1) + ' of ' + messages.length + ' ---');
    lines.push('From: ' + msg.getFrom());
    lines.push('To: ' + msg.getTo());
    const cc = msg.getCc();
    if (cc) {
      lines.push('Cc: ' + cc);
    }
    lines.push('Date: ' + msg.getDate().toISOString());

    const attachments = msg.getAttachments();
    if (attachments.length > 0) {
      const names = attachments.map(function (a) {
        return a.getName();
      });
      lines.push('Attachments (not saved): ' + names.join(', '));
    }

    lines.push('');
    let body = msg.getPlainBody();
    if (body.length > MAX_BODY_CHARS) {
      body = body.substring(0, MAX_BODY_CHARS) + '\n\n[TRUNCATED]';
    }
    lines.push(body.trim());
    lines.push('');
  });

  return lines.join('\n');
}

/**
 * Builds a sortable, filesystem-safe filename: 2026-11-02__subject__threadid.txt
 */
function buildFileName_(thread) {
  const stamp = Utilities.formatDate(
    thread.getLastMessageDate(),
    Session.getScriptTimeZone(),
    'yyyy-MM-dd'
  );
  const subject = (thread.getFirstMessageSubject() || 'no-subject')
    .replace(/[\\/:*?"<>|]/g, '-')
    .replace(/\s+/g, ' ')
    .trim()
    .substring(0, 80);
  return stamp + '__' + subject + '__' + thread.getId() + '.txt';
}

function getOrCreateLabel_(name) {
  return GmailApp.getUserLabelByName(name) || GmailApp.createLabel(name);
}

function getOrCreateFolder_(name) {
  const existing = DriveApp.getFoldersByName(name);
  return existing.hasNext() ? existing.next() : DriveApp.createFolder(name);
}
