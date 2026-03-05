"use client";

import Link from "next/link";
import { Navigation, Footer, FloatingCTA } from "@/components/shared";

const cities = [
  {
    name: "Miami",
    state: "Florida",
    description: "Our headquarters with comprehensive pick-up and delivery services throughout Miami-Dade County.",
  },
  {
    name: "Houston",
    state: "Texas",
    description: "Full service coverage across the greater Houston metropolitan area.",
  },
  {
    name: "Los Angeles",
    state: "California",
    description: "Serving the LA basin and surrounding counties with reliable logistics.",
  },
  {
    name: "New York",
    state: "New York",
    description: "Complete coverage of all five boroughs and surrounding areas.",
  },
  {
    name: "Washington D.C.",
    state: "District of Columbia",
    description: "Service throughout the DC metro area including Northern Virginia and Maryland.",
  },
];

export default function DomesticServicesPage() {
  return (
    <main className="min-h-screen bg-white">
      <Navigation />

      {/* Hero */}
      <section className="pt-32 pb-16 bg-gradient-to-b from-[#E0F2F5] to-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <Link
            href="/services"
            className="inline-flex items-center gap-2 text-[#2E7BBF] mb-4 hover:gap-3 transition-all"
          >
            <svg className="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <line x1="19" y1="12" x2="5" y2="12" />
              <polyline points="12 19 5 12 12 5" />
            </svg>
            Back to Services
          </Link>
          <h1 className="text-4xl sm:text-5xl lg:text-6xl font-bold text-[#0c2940] mb-6">
            Domestic <span className="text-[#2E7BBF]">Services</span>
          </h1>
          <p className="text-lg text-slate-600 max-w-2xl mx-auto">
            Reliable pick-up and delivery services across major U.S. cities with professional handling and coordination.
          </p>
        </div>
      </section>

      {/* Service Overview */}
      <section className="py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid lg:grid-cols-2 gap-16 items-center">
            <div>
              <h2 className="text-3xl font-bold text-[#0c2940] mb-6">
                Local Pick-ups & Deliveries
              </h2>
              <p className="text-slate-600 mb-6">
                We provide comprehensive pick-up and delivery services from local funeral homes
                in major U.S. cities. Our network ensures reliable, timely, and professional
                handling of all domestic shipments.
              </p>
              <p className="text-slate-600 mb-8">
                Whether you need transportation to the airport for an international shipment
                or delivery to a local funeral home, our team coordinates every detail to
                ensure seamless service.
              </p>

              {/* Features */}
              <div className="grid sm:grid-cols-2 gap-4">
                {[
                  "Door-to-door service",
                  "Airport transfers",
                  "Same-day availability",
                  "Professional drivers",
                  "Real-time tracking",
                  "24/7 coordination",
                ].map((feature, i) => (
                  <div key={i} className="flex items-center gap-2">
                    <svg className="w-5 h-5 text-[#4A9BA8]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                      <polyline points="20 6 9 17 4 12" />
                    </svg>
                    <span className="text-slate-700">{feature}</span>
                  </div>
                ))}
              </div>
            </div>

            {/* Service Card */}
            <div className="bg-gradient-to-br from-[#2E7BBF] to-[#4A9BA8] text-white rounded-3xl p-8 lg:p-12">
              <div className="text-center mb-8">
                <div className="inline-flex items-center justify-center w-20 h-20 bg-white/10 rounded-full mb-4">
                  <svg className="w-10 h-10" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <rect x="1" y="3" width="15" height="13" />
                    <polygon points="16 8 20 8 23 11 23 16 16 16 16 8" />
                    <circle cx="5.5" cy="18.5" r="2.5" />
                    <circle cx="18.5" cy="18.5" r="2.5" />
                  </svg>
                </div>
                <h3 className="text-2xl font-bold mb-2">Nationwide Coverage</h3>
                <p className="text-white/60">Professional service across the U.S.</p>
              </div>

              <div className="space-y-4">
                {[
                  { label: "Response Time", value: "< 2 Hours" },
                  { label: "Service Areas", value: "5+ Major Cities" },
                  { label: "Availability", value: "24/7" },
                  { label: "Additional Fees", value: "$0" },
                ].map((item, i) => (
                  <div key={i} className="flex justify-between items-center py-3 border-b border-white/10 last:border-0">
                    <span className="text-white/70">{item.label}</span>
                    <span className="font-bold text-[#E0F2F5]">{item.value}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Cities Grid */}
      <section className="py-16 bg-slate-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-[#0c2940] text-center mb-4">
            Service Areas
          </h2>
          <p className="text-slate-600 text-center mb-12 max-w-2xl mx-auto">
            We provide local pick-up and delivery services in these major metropolitan areas.
          </p>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {cities.map((city, i) => (
              <div
                key={i}
                className="bg-white rounded-xl p-6 shadow-sm border border-slate-100 hover:shadow-lg transition-shadow"
              >
                <div className="flex items-start gap-4">
                  <div className="w-12 h-12 bg-[#E0F2F5] rounded-full flex items-center justify-center flex-shrink-0">
                    <svg className="w-6 h-6 text-[#2E7BBF]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                      <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z" />
                      <circle cx="12" cy="10" r="3" />
                    </svg>
                  </div>
                  <div>
                    <h3 className="font-bold text-[#0c2940]">{city.name}</h3>
                    <p className="text-sm text-[#2E7BBF] mb-2">{city.state}</p>
                    <p className="text-slate-600 text-sm">{city.description}</p>
                  </div>
                </div>
              </div>
            ))}
          </div>

          <div className="text-center mt-8">
            <p className="text-slate-500 text-sm">
              Don&apos;t see your area? Contact us - we can arrange service in many additional locations.
            </p>
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-16 bg-[#0c2940] text-white">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-3xl sm:text-4xl font-bold mb-6">
            Need Domestic Service?
          </h2>
          <p className="text-white/70 mb-8">
            Contact us for reliable pick-up and delivery anywhere in the U.S.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link
              href="/contact"
              className="bg-white text-[#0c2940] px-8 py-4 rounded-full font-bold hover:shadow-xl transition-all"
            >
              Request Service
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
