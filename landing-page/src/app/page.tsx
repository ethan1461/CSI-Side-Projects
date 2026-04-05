"use client";

import { useState, useEffect, useRef } from "react";
import Image from "next/image";
import Link from "next/link";
import {
  Navigation,
  Footer,
  FloatingCTA,
  PlaneIntroAnimation,
} from "@/components/shared";

// Scroll animation hook
function useScrollAnimation() {
  const ref = useRef<HTMLDivElement>(null);
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setIsVisible(true);
        }
      },
      { threshold: 0.1 }
    );

    if (ref.current) {
      observer.observe(ref.current);
    }

    return () => observer.disconnect();
  }, []);

  return { ref, isVisible };
}

// Animated section wrapper
function AnimatedSection({
  children,
  className = "",
  delay = 0,
}: {
  children: React.ReactNode;
  className?: string;
  delay?: number;
}) {
  const { ref, isVisible } = useScrollAnimation();

  return (
    <div
      ref={ref}
      className={`transition-all duration-700 ease-out ${className}`}
      style={{
        opacity: isVisible ? 1 : 0,
        transform: isVisible ? "translateY(0)" : "translateY(30px)",
        transitionDelay: `${delay}ms`,
      }}
    >
      {children}
    </div>
  );
}

// Hero Section with animation
function HeroSection() {
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  return (
    <section className="relative min-h-screen gradient-hero bg-pattern overflow-hidden pt-32 lg:pt-40">
      {/* Animated plane in background */}
      <div className="absolute top-1/4 animate-plane-fly">
        <svg className="w-8 h-8 text-[#2E7BBF]/20" viewBox="0 0 24 24" fill="currentColor">
          <path d="M21 16v-2l-8-5V3.5c0-.83-.67-1.5-1.5-1.5S10 2.67 10 3.5V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z" />
        </svg>
      </div>

      <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-20">
        <div className="grid lg:grid-cols-2 gap-12 items-center">
          {/* Left Content */}
          <div className="text-center lg:text-left">
            {/* Badge */}
            <div
              className={`inline-flex items-center gap-2 bg-white border border-[#B5DEE5] rounded-full px-4 py-2 mb-6 shadow-sm transition-all duration-700 ${
                mounted ? "opacity-100 translate-y-0" : "opacity-0 translate-y-4"
              }`}
            >
              <span className="w-2 h-2 bg-green-500 rounded-full animate-pulse" />
              <span className="text-[#2E7BBF] text-sm font-medium">
                100% Female Owned & Operated Since 2000
              </span>
            </div>

            <h1
              className={`text-4xl sm:text-5xl lg:text-6xl font-bold text-[#0c2940] leading-tight mb-6 transition-all duration-700 delay-100 ${
                mounted ? "opacity-100 translate-y-0" : "opacity-0 translate-y-4"
              }`}
            >
              Human Remains{" "}
              <span className="text-[#2E7BBF]">Transport Services</span>
            </h1>

            <p
              className={`text-lg sm:text-xl text-slate-600 mb-4 max-w-xl mx-auto lg:mx-0 transition-all duration-700 delay-200 ${
                mounted ? "opacity-100 translate-y-0" : "opacity-0 translate-y-4"
              }`}
            >
              Serving the funeral care industry for over{" "}
              <span className="font-semibold text-[#2E7BBF]">24 years</span>.
            </p>

            <p
              className={`text-slate-500 mb-8 max-w-xl mx-auto lg:mx-0 transition-all duration-700 delay-300 ${
                mounted ? "opacity-100 translate-y-0" : "opacity-0 translate-y-4"
              }`}
            >
              Let Cargo Sales International handle the logistics, so you can focus
              on what matters most - caring for your families. Available 24/7.
            </p>

            {/* CTA Buttons */}
            <div
              className={`flex flex-col sm:flex-row gap-4 justify-center lg:justify-start mb-8 transition-all duration-700 delay-400 ${
                mounted ? "opacity-100 translate-y-0" : "opacity-0 translate-y-4"
              }`}
            >
              <Link
                href="/contact"
                className="group relative bg-[#2E7BBF] text-white px-8 py-4 rounded-full font-bold text-lg shadow-lg shadow-[#2E7BBF]/30 hover:bg-[#1E5A8F] hover:shadow-xl hover:shadow-[#2E7BBF]/40 transition-all duration-300 flex items-center justify-center gap-2"
              >
                <svg className="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z" />
                </svg>
                Book a Shipment
                <svg className="w-4 h-4 group-hover:translate-x-1 transition-transform" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <line x1="5" y1="12" x2="19" y2="12" />
                  <polyline points="12 5 19 12 12 19" />
                </svg>
              </Link>
              <a
                href="tel:+18662872583"
                className="group bg-white text-[#2E7BBF] border-2 border-[#2E7BBF] px-8 py-4 rounded-full font-bold text-lg hover:bg-[#E0F2F5] transition-all duration-300 flex items-center justify-center gap-2"
              >
                <svg className="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z" />
                </svg>
                Call Now
              </a>
            </div>

            {/* Trust badges */}
            <div
              className={`flex flex-wrap justify-center lg:justify-start gap-6 text-sm transition-all duration-700 delay-500 ${
                mounted ? "opacity-100 translate-y-0" : "opacity-0 translate-y-4"
              }`}
            >
              {["NO Booking Fees", "24/7 Live Support", "We're Not a Call Center"].map((item, i) => (
                <div key={i} className="flex items-center gap-2 text-slate-600">
                  <svg className="w-5 h-5 text-green-500" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <polyline points="20 6 9 17 4 12" />
                  </svg>
                  <span>{item}</span>
                </div>
              ))}
            </div>
          </div>

          {/* Right Content - Stats Card */}
          <div
            className={`transition-all duration-700 delay-300 ${
              mounted ? "opacity-100 translate-x-0" : "opacity-0 translate-x-8"
            }`}
          >
            <div className="bg-white rounded-3xl p-8 lg:p-10 shadow-xl border border-slate-100">
              <h3 className="text-[#0c2940] text-xl font-semibold mb-8 text-center">
                Trusted by Funeral Homes Nationwide
              </h3>

              <div className="grid grid-cols-2 gap-6">
                {[
                  { value: "100k+", label: "Cases Safely Shipped" },
                  { value: "24+", label: "Years of Experience" },
                  { value: "24/7", label: "Immediate Attention" },
                  { value: "$0", label: "Additional Costs" },
                ].map((stat, i) => (
                  <div key={i} className="text-center">
                    <div className="text-4xl lg:text-5xl font-bold text-[#2E7BBF] mb-2">
                      {stat.value}
                    </div>
                    <div className="text-slate-500 text-sm">{stat.label}</div>
                  </div>
                ))}
              </div>

              {/* IATA Badge */}
              <div className="mt-8 pt-6 border-t border-slate-100 flex items-center justify-center gap-3">
                <div className="w-10 h-10 bg-[#E0F2F5] rounded-full flex items-center justify-center">
                  <svg className="w-5 h-5 text-[#2E7BBF]" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
                    <path d="M9 12l2 2 4-4" />
                  </svg>
                </div>
                <div>
                  <div className="font-semibold text-[#0c2940]">IATA Certified</div>
                  <div className="text-xs text-slate-500">CNS - An IATA Company</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Wave divider */}
      <div className="absolute bottom-0 left-0 right-0">
        <svg viewBox="0 0 1440 120" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path
            d="M0 120L60 110C120 100 240 80 360 70C480 60 600 60 720 65C840 70 960 80 1080 85C1200 90 1320 90 1380 85L1440 80V120H0Z"
            fill="white"
          />
        </svg>
      </div>
    </section>
  );
}

// Services Section
function ServicesSection() {
  const services = [
    {
      icon: (
        <svg className="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <circle cx="12" cy="12" r="10" />
          <line x1="2" y1="12" x2="22" y2="12" />
          <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" />
        </svg>
      ),
      title: "International & Domestic Shipping",
      description: "Versatile shipping options for smooth and secure transportation worldwide.",
      link: "/services",
    },
    {
      icon: (
        <svg className="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />
          <polyline points="14 2 14 8 20 8" />
          <line x1="16" y1="13" x2="8" y2="13" />
          <line x1="16" y1="17" x2="8" y2="17" />
        </svg>
      ),
      title: "Consular Paperwork",
      description: "Translations, apostilles, and legalization for consular clearance.",
      link: "/services",
    },
    {
      icon: (
        <svg className="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <rect x="1" y="3" width="15" height="13" />
          <polygon points="16 8 20 8 23 11 23 16 16 16 16 8" />
          <circle cx="5.5" cy="18.5" r="2.5" />
          <circle cx="18.5" cy="18.5" r="2.5" />
        </svg>
      ),
      title: "Local Pick-ups & Deliveries",
      description: "Services in Miami, Houston, Los Angeles, New York and Washington DC.",
      link: "/services",
    },
    {
      icon: (
        <svg className="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
          <path d="M9 12l2 2 4-4" />
        </svg>
      ),
      title: "Customs Clearance",
      description: "Expert navigation of international regulations and customs procedures.",
      link: "/services",
    },
  ];

  return (
    <section className="section-padding bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <AnimatedSection className="text-center max-w-3xl mx-auto mb-16">
          <span className="inline-block bg-[#E0F2F5] text-[#2E7BBF] rounded-full px-4 py-2 text-sm font-medium mb-4">
            Our Services
          </span>
          <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold text-[#0c2940] mb-6">
            Comprehensive <span className="text-[#2E7BBF]">Funeral Logistics</span>
          </h2>
          <p className="text-lg text-slate-600">
            Our multilingual team handles all arrangements for domestic and international shipments.
          </p>
        </AnimatedSection>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
          {services.map((service, index) => (
            <AnimatedSection key={index} delay={index * 100}>
              <Link
                href={service.link}
                className="group block bg-white border border-slate-200 rounded-2xl p-6 hover:shadow-xl hover:border-[#2E7BBF]/20 transition-all duration-300 h-full"
              >
                <div className="w-14 h-14 bg-[#E0F2F5] rounded-xl flex items-center justify-center mb-5 text-[#2E7BBF] group-hover:bg-[#2E7BBF] group-hover:text-white transition-colors duration-300">
                  {service.icon}
                </div>
                <h3 className="text-lg font-bold text-[#0c2940] mb-3 group-hover:text-[#2E7BBF] transition-colors">
                  {service.title}
                </h3>
                <p className="text-slate-600 text-sm">{service.description}</p>
              </Link>
            </AnimatedSection>
          ))}
        </div>

        <AnimatedSection delay={400} className="text-center mt-12">
          <Link
            href="/services"
            className="inline-flex items-center gap-2 text-[#2E7BBF] font-semibold hover:gap-3 transition-all"
          >
            View All Services
            <svg className="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <line x1="5" y1="12" x2="19" y2="12" />
              <polyline points="12 5 19 12 12 19" />
            </svg>
          </Link>
        </AnimatedSection>
      </div>
    </section>
  );
}

// Why Choose Us Section
function WhyUsSection() {
  const reasons = [
    {
      number: "100k+",
      title: "Cases Safely Shipped",
      description: "Trust our expertise for secure and reliable transportation.",
    },
    {
      number: "24+",
      title: "Years of Experience",
      description: "Extensive network and proven track record with airlines.",
    },
    {
      number: "24/7",
      title: "Live Support",
      description: "Our dedicated team is available around the clock.",
    },
  ];

  return (
    <section className="section-padding bg-[#0c2940] text-white relative overflow-hidden">
      {/* Background pattern */}
      <div className="absolute inset-0 opacity-5">
        <div className="absolute inset-0" style={{
          backgroundImage: `url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='white' fill-opacity='1'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/svg%3E")`,
        }} />
      </div>

      <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <AnimatedSection className="text-center max-w-3xl mx-auto mb-16">
          <span className="inline-block bg-white/10 text-white rounded-full px-4 py-2 text-sm font-medium mb-4">
            Why Choose Us
          </span>
          <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold mb-6">
            We Provide an <span className="text-[#6BB5C0]">Extraordinary Experience</span>
          </h2>
          <p className="text-lg text-white/70">
            We&apos;re not a call center. We&apos;re dedicated professionals committed to exceptional service.
          </p>
        </AnimatedSection>

        <div className="grid md:grid-cols-3 gap-8">
          {reasons.map((item, index) => (
            <AnimatedSection key={index} delay={index * 100}>
              <div className="text-center p-8 bg-white/5 rounded-2xl border border-white/10 hover:bg-white/10 transition-colors">
                <div className="text-5xl lg:text-6xl font-bold text-[#6BB5C0] mb-4">
                  {item.number}
                </div>
                <h3 className="text-xl font-bold mb-3">{item.title}</h3>
                <p className="text-white/70">{item.description}</p>
              </div>
            </AnimatedSection>
          ))}
        </div>

        <AnimatedSection delay={300} className="text-center mt-12">
          <Link
            href="/about"
            className="inline-flex items-center gap-2 bg-white text-[#0c2940] px-8 py-4 rounded-full font-bold hover:shadow-xl transition-all"
          >
            Learn More About Us
            <svg className="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <line x1="5" y1="12" x2="19" y2="12" />
              <polyline points="12 5 19 12 12 19" />
            </svg>
          </Link>
        </AnimatedSection>
      </div>
    </section>
  );
}

// CTA Section
function CTASection() {
  return (
    <section className="section-padding bg-gradient-to-br from-[#E0F2F5] to-white">
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <AnimatedSection>
          <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold text-[#0c2940] mb-6">
            Ready to <span className="text-[#2E7BBF]">Get Started?</span>
          </h2>
          <p className="text-lg text-slate-600 mb-8 max-w-2xl mx-auto">
            We simplify the booking process for funeral homes on all domestic & international
            shipments, giving you more time to assist families.
          </p>

          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link
              href="/contact"
              className="group bg-[#2E7BBF] text-white px-8 py-4 rounded-full font-bold text-lg shadow-lg shadow-[#2E7BBF]/30 hover:bg-[#1E5A8F] hover:shadow-xl transition-all flex items-center justify-center gap-2"
            >
              Book a Shipment Now
              <svg className="w-5 h-5 group-hover:translate-x-1 transition-transform" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <line x1="5" y1="12" x2="19" y2="12" />
                <polyline points="12 5 19 12 12 19" />
              </svg>
            </Link>
            <a
              href="tel:+18662872583"
              className="bg-white text-[#2E7BBF] border-2 border-[#2E7BBF] px-8 py-4 rounded-full font-bold text-lg hover:bg-[#E0F2F5] transition-all flex items-center justify-center gap-2"
            >
              <svg className="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z" />
              </svg>
              +1 (866) 287-2583
            </a>
          </div>

          <p className="mt-6 text-sm text-slate-500 flex items-center justify-center gap-2">
            <span className="w-2 h-2 bg-green-500 rounded-full animate-pulse" />
            Live team available 24/7/365
          </p>
        </AnimatedSection>
      </div>
    </section>
  );
}

// Main Page Component
export default function Home() {
  const [showIntro, setShowIntro] = useState(true);
  const [introComplete, setIntroComplete] = useState(false);

  // Check if user has seen the intro recently
  useEffect(() => {
    const hasSeenIntro = sessionStorage.getItem("csi-intro-seen");
    if (hasSeenIntro) {
      setShowIntro(false);
      setIntroComplete(true);
    }
  }, []);

  const handleIntroComplete = () => {
    setIntroComplete(true);
    sessionStorage.setItem("csi-intro-seen", "true");
    setTimeout(() => setShowIntro(false), 500);
  };

  return (
    <main className="min-h-screen">
      {showIntro && !introComplete && (
        <PlaneIntroAnimation onComplete={handleIntroComplete} />
      )}
      <Navigation />
      <HeroSection />
      <ServicesSection />
      <WhyUsSection />
      <CTASection />
      <Footer />
      <FloatingCTA />
    </main>
  );
}
