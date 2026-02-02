import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Cargo Sales International | End-to-End Human Remains Logistics",
  description:
    "CSI is your trusted partner for air freight logistics of human remains. FREE service with 24/7 support, 5-6 routing options, and complete international documentation handling. Trusted by funeral homes nationwide.",
  keywords: [
    "human remains shipping",
    "funeral home logistics",
    "air freight",
    "repatriation services",
    "international shipping",
    "cremated remains",
  ],
  openGraph: {
    title: "Cargo Sales International | Trusted Human Remains Logistics",
    description:
      "FREE end-to-end shipment orchestration for funeral homes. 24/7 live agents, 5-6 routing options, complete international support.",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="scroll-smooth">
      <body className="font-sans antialiased">{children}</body>
    </html>
  );
}
