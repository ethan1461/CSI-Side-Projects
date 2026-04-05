"use client";

import Link from "next/link";
import { Navigation, Footer, FloatingCTA } from "@/components/shared";

const services = [
  {
    title: "International & Domestic Shipping",
    description: "Simplify your logistics needs with our versatile shipping options, enabling smooth and secure transportation both internationally and domestically. We work with major airlines to provide reliable routing.",
    icon: (
      <svg className="w-10 h-10" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
        <circle cx="12" cy="12" r="10" />
        <line x1="2" y1="12" x2="22" y2="12" />
        <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" />
      </svg>
    ),
    link: "/services/international",
    features: ["Multiple routing options", "Competitive rates", "Real-time tracking"],
  },
  {
    title: "Confirmed Itineraries",
    description: "We ensure peace of mind with our meticulously confirmed itineraries, assuring you of precise and reliable scheduling for seamless international and domestic transportation.",
    icon: (
      <svg className="w-10 h-10" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
        <rect x="3" y="4" width="18" height="18" rx="2" ry="2" />
        <line x1="16" y1="2" x2="16" y2="6" />
        <line x1="8" y1="2" x2="8" y2="6" />
        <line x1="3" y1="10" x2="21" y2="10" />
      </svg>
    ),
    features: ["Precise scheduling", "Flight confirmations", "Backup routing"],
  },
  {
    title: "Local Pick-ups & Deliveries",
    description: "Pick-up and delivery services from local funeral homes in major U.S. cities including Miami, Houston, Los Angeles, New York, and Washington DC.",
    icon: (
      <svg className="w-10 h-10" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
        <rect x="1" y="3" width="15" height="13" />
        <polygon points="16 8 20 8 23 11 23 16 16 16 16 8" />
        <circle cx="5.5" cy="18.5" r="2.5" />
        <circle cx="18.5" cy="18.5" r="2.5" />
      </svg>
    ),
    link: "/services/domestic",
    features: ["Major U.S. cities", "Reliable timing", "Professional handling"],
  },
  {
    title: "Prepaid Flight Charges",
    description: "All shipments are prepaid on our account, eliminating the necessity to bring payments to the airport. No surprise fees, no hassle.",
    icon: (
      <svg className="w-10 h-10" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
        <rect x="1" y="4" width="22" height="16" rx="2" ry="2" />
        <line x1="1" y1="10" x2="23" y2="10" />
      </svg>
    ),
    features: ["No airport payments", "Transparent pricing", "Prepaid convenience"],
  },
  {
    title: "Consular Paperwork",
    description: "We facilitate translations, apostilles, and legalization of international paperwork for consular clearance. Our team handles all documentation requirements.",
    icon: (
      <svg className="w-10 h-10" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />
        <polyline points="14 2 14 8 20 8" />
        <line x1="16" y1="13" x2="8" y2="13" />
        <line x1="16" y1="17" x2="8" y2="17" />
      </svg>
    ),
    features: ["Translations", "Apostilles", "Consulate liaison"],
  },
  {
    title: "Customs Clearance",
    description: "Trust us to handle the intricacies of customs procedures, ensuring a hassle-free experience as we expertly navigate international regulations.",
    icon: (
      <svg className="w-10 h-10" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
        <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
        <path d="M9 12l2 2 4-4" />
      </svg>
    ),
    features: ["Compliance expertise", "Swift processing", "Regulation navigation"],
  },
  {
    title: "Cancellation & Delay Updates",
    description: "We prioritize clear communication, keeping you updated and well-informed about any potential cancellations or delays throughout the process.",
    icon: (
      <svg className="w-10 h-10" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
        <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9" />
        <path d="M13.73 21a2 2 0 0 1-3.46 0" />
      </svg>
    ),
    features: ["Real-time alerts", "Proactive communication", "Rebooking assistance"],
  },
];

export default function ServicesPage() {
  return (
    <main className="min-h-screen bg-white">
      <Navigation />

      {/* Hero */}
      <section className="pt-32 pb-16 bg-gradient-to-b from-[#E0F2F5] to-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <span className="inline-block bg-white text-[#2E7BBF] rounded-full px-4 py-2 text-sm font-medium mb-4 shadow-sm">
            What We Offer
          </span>
          <h1 className="text-4xl sm:text-5xl lg:text-6xl font-bold text-[#0c2940] mb-6">
            Our <span className="text-[#2E7BBF]">Services</span>
          </h1>
          <p className="text-lg text-slate-600 max-w-2xl mx-auto">
            Comprehensive funeral logistics services backed by 24+ years of experience.
            Our multilingual team is ready to assist with all your shipping needs.
          </p>
        </div>
      </section>

      {/* Services Grid */}
      <section className="py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {services.map((service, index) => (
              <div
                key={index}
                className="group bg-white border border-slate-200 rounded-2xl p-6 hover:shadow-xl hover:border-[#2E7BBF]/20 transition-all duration-300"
              >
                <div className="w-16 h-16 bg-[#E0F2F5] rounded-xl flex items-center justify-center mb-5 text-[#2E7BBF] group-hover:bg-[#2E7BBF] group-hover:text-white transition-colors duration-300">
                  {service.icon}
                </div>
                <h3 className="text-xl font-bold text-[#0c2940] mb-3 group-hover:text-[#2E7BBF] transition-colors">
                  {service.title}
                </h3>
                <p className="text-slate-600 mb-4">{service.description}</p>
                <ul className="space-y-2">
                  {service.features.map((feature, i) => (
                    <li key={i} className="flex items-center gap-2 text-sm text-slate-500">
                      <svg className="w-4 h-4 text-[#4A9BA8]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                        <polyline points="20 6 9 17 4 12" />
                      </svg>
                      {feature}
                    </li>
                  ))}
                </ul>
                {service.link && (
                  <Link
                    href={service.link}
                    className="inline-flex items-center gap-2 text-[#2E7BBF] font-medium mt-4 hover:gap-3 transition-all"
                  >
                    Learn more
                    <svg className="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                      <line x1="5" y1="12" x2="19" y2="12" />
                      <polyline points="12 5 19 12 12 19" />
                    </svg>
                  </Link>
                )}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-16 bg-[#0c2940] text-white">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-3xl sm:text-4xl font-bold mb-6">
            Ready to Get Started?
          </h2>
          <p className="text-white/70 mb-8">
            Contact us today for a quote or to learn more about our services.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link
              href="/book"
              className="bg-white text-[#0c2940] px-8 py-4 rounded-full font-bold hover:shadow-xl transition-all"
            >
              Book a Shipment
            </Link>
            <a
              href="tel:+18662872583"
              className="border-2 border-white text-white px-8 py-4 rounded-full font-bold hover:bg-white/10 transition-all"
            >
              Call +1 (866) 287-2583
            </a>
          </div>
        </div>
      </section>

      <Footer />
      <FloatingCTA />
    </main>
  );
}
