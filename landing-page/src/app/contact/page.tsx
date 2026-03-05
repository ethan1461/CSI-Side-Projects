"use client";

import { useState } from "react";
import { Navigation, Footer, FloatingCTA } from "@/components/shared";

export default function ContactPage() {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    phone: "",
    company: "",
    message: "",
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // Form submission logic would go here
    alert("Thank you for your message. We will contact you shortly.");
  };

  return (
    <main className="min-h-screen bg-white">
      <Navigation />

      {/* Hero */}
      <section className="pt-32 pb-16 bg-gradient-to-b from-[#E0F2F5] to-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <span className="inline-block bg-white text-[#2E7BBF] rounded-full px-4 py-2 text-sm font-medium mb-4 shadow-sm">
            Get In Touch
          </span>
          <h1 className="text-4xl sm:text-5xl lg:text-6xl font-bold text-[#0c2940] mb-6">
            Contact <span className="text-[#2E7BBF]">Us</span>
          </h1>
          <p className="text-lg text-slate-600 max-w-2xl mx-auto">
            Ready to book a shipment or have questions? Our team is available
            24/7 to assist you.
          </p>
        </div>
      </section>

      {/* Contact Content */}
      <section className="py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid lg:grid-cols-2 gap-16">
            {/* Contact Form */}
            <div>
              <h2 className="text-2xl font-bold text-[#0c2940] mb-6">
                Send Us a Message
              </h2>
              <form onSubmit={handleSubmit} className="space-y-6">
                <div className="grid sm:grid-cols-2 gap-6">
                  <div>
                    <label
                      htmlFor="name"
                      className="block text-sm font-medium text-slate-700 mb-2"
                    >
                      Full Name *
                    </label>
                    <input
                      type="text"
                      id="name"
                      required
                      className="w-full px-4 py-3 border border-slate-300 rounded-lg focus:ring-2 focus:ring-[#2E7BBF] focus:border-transparent outline-none transition-all"
                      value={formData.name}
                      onChange={(e) =>
                        setFormData({ ...formData, name: e.target.value })
                      }
                    />
                  </div>
                  <div>
                    <label
                      htmlFor="email"
                      className="block text-sm font-medium text-slate-700 mb-2"
                    >
                      Email Address *
                    </label>
                    <input
                      type="email"
                      id="email"
                      required
                      className="w-full px-4 py-3 border border-slate-300 rounded-lg focus:ring-2 focus:ring-[#2E7BBF] focus:border-transparent outline-none transition-all"
                      value={formData.email}
                      onChange={(e) =>
                        setFormData({ ...formData, email: e.target.value })
                      }
                    />
                  </div>
                </div>
                <div className="grid sm:grid-cols-2 gap-6">
                  <div>
                    <label
                      htmlFor="phone"
                      className="block text-sm font-medium text-slate-700 mb-2"
                    >
                      Phone Number
                    </label>
                    <input
                      type="tel"
                      id="phone"
                      className="w-full px-4 py-3 border border-slate-300 rounded-lg focus:ring-2 focus:ring-[#2E7BBF] focus:border-transparent outline-none transition-all"
                      value={formData.phone}
                      onChange={(e) =>
                        setFormData({ ...formData, phone: e.target.value })
                      }
                    />
                  </div>
                  <div>
                    <label
                      htmlFor="company"
                      className="block text-sm font-medium text-slate-700 mb-2"
                    >
                      Funeral Home / Company
                    </label>
                    <input
                      type="text"
                      id="company"
                      className="w-full px-4 py-3 border border-slate-300 rounded-lg focus:ring-2 focus:ring-[#2E7BBF] focus:border-transparent outline-none transition-all"
                      value={formData.company}
                      onChange={(e) =>
                        setFormData({ ...formData, company: e.target.value })
                      }
                    />
                  </div>
                </div>
                <div>
                  <label
                    htmlFor="message"
                    className="block text-sm font-medium text-slate-700 mb-2"
                  >
                    Message *
                  </label>
                  <textarea
                    id="message"
                    rows={5}
                    required
                    className="w-full px-4 py-3 border border-slate-300 rounded-lg focus:ring-2 focus:ring-[#2E7BBF] focus:border-transparent outline-none transition-all resize-none"
                    value={formData.message}
                    onChange={(e) =>
                      setFormData({ ...formData, message: e.target.value })
                    }
                  />
                </div>
                <button
                  type="submit"
                  className="w-full bg-[#2E7BBF] text-white py-4 rounded-full font-bold hover:bg-[#1E5A8F] transition-colors"
                >
                  Send Message
                </button>
              </form>
            </div>

            {/* Contact Info */}
            <div>
              <h2 className="text-2xl font-bold text-[#0c2940] mb-6">
                Contact Information
              </h2>

              {/* Quick Contact Card */}
              <div className="bg-[#0c2940] text-white rounded-2xl p-8 mb-8">
                <h3 className="text-xl font-bold mb-6">Call Us Now</h3>
                <div className="space-y-4">
                  <a
                    href="tel:+18662872583"
                    className="flex items-center gap-4 text-lg hover:text-[#6BB5C0] transition-colors"
                  >
                    <div className="w-12 h-12 bg-white/10 rounded-full flex items-center justify-center">
                      <svg
                        className="w-6 h-6"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="2"
                      >
                        <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z" />
                      </svg>
                    </div>
                    <div>
                      <div className="text-white/60 text-sm">Toll Free</div>
                      <div className="font-bold">+1 (866) 287-2583</div>
                    </div>
                  </a>
                  <a
                    href="tel:+13057169991"
                    className="flex items-center gap-4 text-lg hover:text-[#6BB5C0] transition-colors"
                  >
                    <div className="w-12 h-12 bg-white/10 rounded-full flex items-center justify-center">
                      <svg
                        className="w-6 h-6"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="2"
                      >
                        <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z" />
                      </svg>
                    </div>
                    <div>
                      <div className="text-white/60 text-sm">Direct</div>
                      <div className="font-bold">+1 (305) 716-9991</div>
                    </div>
                  </a>
                </div>
                <div className="mt-6 pt-6 border-t border-white/10">
                  <div className="flex items-center gap-2 text-[#6BB5C0]">
                    <svg
                      className="w-5 h-5"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      strokeWidth="2"
                    >
                      <circle cx="12" cy="12" r="10" />
                      <polyline points="12 6 12 12 16 14" />
                    </svg>
                    <span className="font-medium">Available 24/7</span>
                  </div>
                </div>
              </div>

              {/* Additional Info */}
              <div className="space-y-6">
                <div className="flex items-start gap-4">
                  <div className="w-12 h-12 bg-[#E0F2F5] rounded-full flex items-center justify-center flex-shrink-0">
                    <svg
                      className="w-6 h-6 text-[#2E7BBF]"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      strokeWidth="2"
                    >
                      <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" />
                      <polyline points="22,6 12,13 2,6" />
                    </svg>
                  </div>
                  <div>
                    <h4 className="font-semibold text-[#0c2940]">Email</h4>
                    <a
                      href="mailto:contact@cargosalesintl.com"
                      className="text-slate-600 hover:text-[#2E7BBF] transition-colors"
                    >
                      contact@cargosalesintl.com
                    </a>
                  </div>
                </div>

                <div className="flex items-start gap-4">
                  <div className="w-12 h-12 bg-[#E0F2F5] rounded-full flex items-center justify-center flex-shrink-0">
                    <svg
                      className="w-6 h-6 text-[#2E7BBF]"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      strokeWidth="2"
                    >
                      <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z" />
                      <circle cx="12" cy="10" r="3" />
                    </svg>
                  </div>
                  <div>
                    <h4 className="font-semibold text-[#0c2940]">Location</h4>
                    <p className="text-slate-600">Miami, Florida, USA</p>
                  </div>
                </div>

                <div className="flex items-start gap-4">
                  <div className="w-12 h-12 bg-[#E0F2F5] rounded-full flex items-center justify-center flex-shrink-0">
                    <svg
                      className="w-6 h-6 text-[#2E7BBF]"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      strokeWidth="2"
                    >
                      <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
                    </svg>
                  </div>
                  <div>
                    <h4 className="font-semibold text-[#0c2940]">Languages</h4>
                    <p className="text-slate-600">
                      English, Spanish, Portuguese, French, Creole
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* FAQ Section */}
      <section className="py-16 bg-slate-50">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-[#0c2940] text-center mb-12">
            Frequently Asked Questions
          </h2>
          <div className="space-y-6">
            {[
              {
                q: "How quickly can you arrange a shipment?",
                a: "We can often arrange same-day or next-day shipments depending on airline availability and documentation readiness. Our team works around the clock to ensure timely service.",
              },
              {
                q: "Do you handle international paperwork?",
                a: "Yes, we facilitate translations, apostilles, and legalization of international paperwork for consular clearance. Our team handles all documentation requirements.",
              },
              {
                q: "Are there any hidden fees?",
                a: "No. All shipments are prepaid on our account with no booking fees or additional costs. We believe in transparent pricing with no surprises.",
              },
              {
                q: "What areas do you serve?",
                a: "We offer international shipping worldwide and domestic services throughout the United States, with local pick-up and delivery in major cities including Miami, Houston, Los Angeles, New York, and Washington DC.",
              },
            ].map((faq, i) => (
              <div
                key={i}
                className="bg-white rounded-xl p-6 shadow-sm border border-slate-100"
              >
                <h3 className="font-bold text-[#0c2940] mb-2">{faq.q}</h3>
                <p className="text-slate-600">{faq.a}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      <Footer />
      <FloatingCTA />
    </main>
  );
}
