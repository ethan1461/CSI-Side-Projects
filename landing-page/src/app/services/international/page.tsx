"use client";

import Link from "next/link";
import { Navigation, Footer, FloatingCTA } from "@/components/shared";

const regions = [
  {
    name: "Central America & Caribbean",
    countries: "Mexico, Guatemala, Honduras, Jamaica, Haiti, Dominican Republic, Cuba, and more",
    icon: (
      <svg className="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
        <circle cx="12" cy="12" r="10" />
        <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" />
      </svg>
    ),
  },
  {
    name: "South America",
    countries: "Brazil, Colombia, Venezuela, Peru, Ecuador, Argentina, Chile, and more",
    icon: (
      <svg className="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
        <circle cx="12" cy="12" r="10" />
        <line x1="2" y1="12" x2="22" y2="12" />
      </svg>
    ),
  },
  {
    name: "Europe",
    countries: "United Kingdom, Germany, France, Italy, Spain, Poland, and more",
    icon: (
      <svg className="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
        <circle cx="12" cy="12" r="10" />
        <path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10" />
      </svg>
    ),
  },
  {
    name: "Africa",
    countries: "Nigeria, Ghana, Ethiopia, Kenya, South Africa, Egypt, and more",
    icon: (
      <svg className="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
        <circle cx="12" cy="12" r="10" />
        <path d="M12 2v20M2 12h20" />
      </svg>
    ),
  },
  {
    name: "Asia & Middle East",
    countries: "India, Philippines, China, Japan, UAE, Saudi Arabia, and more",
    icon: (
      <svg className="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
        <circle cx="12" cy="12" r="10" />
        <path d="M12 2a15.3 15.3 0 0 0-4 10 15.3 15.3 0 0 0 4 10" />
      </svg>
    ),
  },
];

const services = [
  {
    title: "Customs Clearance",
    description: "We navigate complex customs procedures and international regulations - you just make one call.",
  },
  {
    title: "Consular Documentation",
    description: "Translations, apostilles, legalization - we handle all consular requirements so you don't have to.",
  },
  {
    title: "Strategic Airline Alliances",
    description: "Our 50+ airline partnerships mean optimal routing and pricing without you shopping around.",
  },
  {
    title: "Real-Time Tracking",
    description: "Stay informed without chasing updates - we keep you posted throughout the journey.",
  },
];

export default function InternationalServicesPage() {
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
            International <span className="text-[#2E7BBF]">Shipping</span>
          </h1>
          <p className="text-lg text-slate-600 max-w-2xl mx-auto">
            Consulates, translations, customs, regulations - we handle it all. You focus on
            your families, we&apos;ll handle the complexity of international shipping.
          </p>
        </div>
      </section>

      {/* Main Content */}
      <section className="py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid lg:grid-cols-2 gap-16 items-start">
            {/* Left - Info */}
            <div>
              {/* Key Value Proposition */}
              <div className="bg-[#E0F2F5] rounded-xl p-6 mb-8 border-l-4 border-[#2E7BBF]">
                <h3 className="font-bold text-[#0c2940] text-lg mb-2">
                  You Don&apos;t Need to Be an Expert - We Are
                </h3>
                <p className="text-slate-600">
                  International shipping involves consulates, translations, apostilles, customs
                  regulations, and complex logistics. <strong>That&apos;s our specialty, not yours.</strong> Focus
                  on caring for your families while we handle the complexity.
                </p>
              </div>

              <h2 className="text-3xl font-bold text-[#0c2940] mb-6">
                Global Reach, Local Expertise
              </h2>
              <p className="text-slate-600 mb-6">
                With over 24 years of experience shipping to destinations worldwide, Cargo Sales
                International has established strategic alliances with numerous airlines that
                enable us to offer the best routing at the most affordable prices.
              </p>
              <p className="text-slate-600 mb-8">
                Our multilingual team (English, Spanish, Portuguese, French, and Creole) helps
                funeral homes better serve their families with expertise and care. We handle all
                aspects of international shipping including customs clearance, consular documentation,
                and real-time coordination - so you don&apos;t have to.
              </p>

              {/* Services List */}
              <div className="grid sm:grid-cols-2 gap-6">
                {services.map((service, i) => (
                  <div key={i} className="flex items-start gap-3">
                    <div className="w-8 h-8 bg-[#E0F2F5] rounded-full flex items-center justify-center flex-shrink-0 mt-0.5">
                      <svg className="w-4 h-4 text-[#2E7BBF]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                        <polyline points="20 6 9 17 4 12" />
                      </svg>
                    </div>
                    <div>
                      <h4 className="font-semibold text-[#0c2940]">{service.title}</h4>
                      <p className="text-sm text-slate-600">{service.description}</p>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Right - Stats Card */}
            <div className="bg-[#0c2940] text-white rounded-3xl p-8 lg:p-12">
              <div className="text-center mb-8">
                <div className="inline-flex items-center justify-center w-20 h-20 bg-white/10 rounded-full mb-4">
                  <svg className="w-10 h-10 text-[#6BB5C0]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <circle cx="12" cy="12" r="10" />
                    <line x1="2" y1="12" x2="22" y2="12" />
                    <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" />
                  </svg>
                </div>
                <h3 className="text-2xl font-bold mb-2">Worldwide Coverage</h3>
                <p className="text-white/60">Shipping to destinations across the globe</p>
              </div>

              <div className="grid grid-cols-2 gap-6 mb-8">
                {[
                  { value: "100+", label: "Countries Served" },
                  { value: "50+", label: "Airline Partners" },
                  { value: "100k+", label: "Cases Shipped" },
                  { value: "$0", label: "Hidden Fees" },
                ].map((stat, i) => (
                  <div key={i} className="text-center">
                    <div className="text-3xl font-bold text-[#6BB5C0] mb-1">{stat.value}</div>
                    <div className="text-white/60 text-sm">{stat.label}</div>
                  </div>
                ))}
              </div>

              <div className="pt-6 border-t border-white/10">
                <h4 className="font-semibold mb-3 text-center">Prepaid Flights</h4>
                <p className="text-white/70 text-sm text-center">
                  All shipments are prepaid on our account, eliminating the necessity
                  to bring payments to the airport. No surprise fees, no hassle.
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Regions */}
      <section className="py-16 bg-slate-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-[#0c2940] text-center mb-4">
            Regions We Serve
          </h2>
          <p className="text-slate-600 text-center mb-12 max-w-2xl mx-auto">
            Our international network spans all continents with established relationships
            and routing expertise.
          </p>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {regions.map((region, i) => (
              <div
                key={i}
                className="bg-white rounded-xl p-6 shadow-sm border border-slate-100 hover:shadow-lg hover:border-[#2E7BBF]/20 transition-all"
              >
                <div className="w-14 h-14 bg-[#E0F2F5] rounded-xl flex items-center justify-center mb-4 text-[#2E7BBF]">
                  {region.icon}
                </div>
                <h3 className="font-bold text-[#0c2940] text-lg mb-2">{region.name}</h3>
                <p className="text-slate-600 text-sm">{region.countries}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Process */}
      <section className="py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-3xl font-bold text-[#0c2940] text-center mb-12">
            How It Works
          </h2>

          <div className="grid md:grid-cols-4 gap-8">
            {[
              {
                step: "1",
                title: "Contact Us",
                description: "Call or email with your shipment details",
              },
              {
                step: "2",
                title: "Get Quote",
                description: "Receive transparent pricing with no hidden fees",
              },
              {
                step: "3",
                title: "We Handle It",
                description: "Documentation, booking, and customs clearance",
              },
              {
                step: "4",
                title: "Delivery",
                description: "Real-time tracking until safe arrival",
              },
            ].map((item, i) => (
              <div key={i} className="text-center">
                <div className="w-16 h-16 bg-gradient-to-br from-[#2E7BBF] to-[#4A9BA8] text-white rounded-full flex items-center justify-center mx-auto mb-4 text-2xl font-bold">
                  {item.step}
                </div>
                <h3 className="font-bold text-[#0c2940] mb-2">{item.title}</h3>
                <p className="text-slate-600 text-sm">{item.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-16 bg-gradient-to-br from-[#2E7BBF] to-[#4A9BA8] text-white">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-3xl sm:text-4xl font-bold mb-6">
            Ready to Ship Internationally?
          </h2>
          <p className="text-white/80 mb-8">
            Get a quote today. Our multilingual team is available 24/7 to assist you.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link
              href="/contact"
              className="bg-white text-[#2E7BBF] px-8 py-4 rounded-full font-bold hover:shadow-xl transition-all"
            >
              Get a Quote
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
