"use client";

import Link from "next/link";
import { Navigation, Footer, FloatingCTA } from "@/components/shared";

export default function AboutPage() {
  return (
    <main className="min-h-screen bg-white">
      <Navigation />

      {/* Hero */}
      <section className="pt-32 pb-16 bg-gradient-to-b from-[#E0F2F5] to-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <span className="inline-block bg-white text-[#2E7BBF] rounded-full px-4 py-2 text-sm font-medium mb-4 shadow-sm">
            Our Story
          </span>
          <h1 className="text-4xl sm:text-5xl lg:text-6xl font-bold text-[#0c2940] mb-6">
            About <span className="text-[#2E7BBF]">Cargo Sales International</span>
          </h1>
          <p className="text-lg text-slate-600 max-w-2xl mx-auto">
            100% female owned and operated for the past 24 years, serving the funeral care industry with dedication and expertise.
          </p>
        </div>
      </section>

      {/* Main Content */}
      <section className="py-16">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid lg:grid-cols-2 gap-16 items-center">
            {/* Left - Story */}
            <div>
              <h2 className="text-3xl font-bold text-[#0c2940] mb-6">
                We Are <span className="text-[#2E7BBF]">Not a Call Center</span>
              </h2>
              <p className="text-slate-600 mb-6">
                At Cargo Sales International, we take great pride in offering exceptional
                service and customer support. Whether you require a price quote, assistance
                with crafting an itinerary, or any information, we are here to help.
              </p>
              <p className="text-slate-600 mb-6">
                We&apos;re a team of highly trained professionals who have been serving the
                funeral care industry for over 24 years. We&apos;re committed to bringing you
                top niche assistance and expertise.
              </p>
              <p className="text-slate-600 mb-8">
                We help funeral homes better serve their families with a wide range of shipping services
                custom fit to your needs. You can use our services with NO booking fees &
                at NO additional costs!
              </p>

              {/* Features */}
              <div className="grid sm:grid-cols-2 gap-4">
                {[
                  "NO booking fees",
                  "NO additional costs",
                  "Strategic airline alliances",
                  "Multi-lingual support",
                  "24/7 availability",
                  "Dedicated professionals",
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

            {/* Right - Stats Card */}
            <div className="bg-[#0c2940] text-white rounded-3xl p-8 lg:p-12">
              <div className="text-center mb-8">
                <div className="inline-flex items-center justify-center w-20 h-20 bg-white/10 rounded-full mb-4">
                  <svg className="w-10 h-10 text-[#6BB5C0]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" />
                  </svg>
                </div>
                <h3 className="text-2xl font-bold mb-2">100% Female Owned & Operated</h3>
                <p className="text-white/60">Since 2000</p>
              </div>

              <div className="grid grid-cols-2 gap-6">
                {[
                  { value: "100k+", label: "Cases Shipped" },
                  { value: "24+", label: "Years Experience" },
                  { value: "24/7", label: "Availability" },
                  { value: "$0", label: "Hidden Fees" },
                ].map((stat, i) => (
                  <div key={i} className="text-center">
                    <div className="text-3xl font-bold text-[#6BB5C0] mb-1">{stat.value}</div>
                    <div className="text-white/60 text-sm">{stat.label}</div>
                  </div>
                ))}
              </div>

              <div className="mt-8 pt-6 border-t border-white/10">
                <p className="text-white/70 text-sm text-center italic">
                  &quot;We have strategic alliances with numerous airlines worldwide which
                  enable us to offer you the best routing at the most affordable prices.&quot;
                </p>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Trust Badges */}
      <section className="py-16 bg-slate-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <h2 className="text-2xl font-bold text-[#0c2940] text-center mb-12">
            Certified & Recognized By
          </h2>
          <div className="flex flex-wrap justify-center items-center gap-12">
            <div className="flex items-center gap-3 text-slate-600">
              <div className="w-14 h-14 bg-[#E0F2F5] rounded-full flex items-center justify-center">
                <svg className="w-7 h-7 text-[#2E7BBF]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
                  <path d="M9 12l2 2 4-4" />
                </svg>
              </div>
              <div>
                <div className="font-semibold">U.S. Department of</div>
                <div className="text-sm text-slate-500">Homeland Security</div>
              </div>
            </div>
            <div className="flex items-center gap-3 text-slate-600">
              <div className="w-14 h-14 bg-[#E0F2F5] rounded-full flex items-center justify-center">
                <svg className="w-7 h-7 text-[#2E7BBF]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <circle cx="12" cy="12" r="10" />
                  <line x1="2" y1="12" x2="22" y2="12" />
                  <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" />
                </svg>
              </div>
              <div>
                <div className="font-semibold">CNS - An IATA Company</div>
                <div className="text-sm text-slate-500">IATA Certified</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-16 bg-gradient-to-br from-[#2E7BBF] to-[#4A9BA8] text-white">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h2 className="text-3xl sm:text-4xl font-bold mb-6">
            Ready to Work With Us?
          </h2>
          <p className="text-white/80 mb-8">
            Experience the CSI difference. Let us handle the logistics while you focus on families.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link
              href="/contact"
              className="bg-white text-[#2E7BBF] px-8 py-4 rounded-full font-bold hover:shadow-xl transition-all"
            >
              Contact Us Today
            </Link>
            <Link
              href="/services"
              className="border-2 border-white text-white px-8 py-4 rounded-full font-bold hover:bg-white/10 transition-all"
            >
              View Our Services
            </Link>
          </div>
        </div>
      </section>

      <Footer />
      <FloatingCTA />
    </main>
  );
}
