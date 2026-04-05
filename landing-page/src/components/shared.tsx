"use client";

import { useState, useEffect } from "react";
import Image from "next/image";
import Link from "next/link";

// Plane animation that plays on initial load
export function PlaneIntroAnimation({ onComplete }: { onComplete: () => void }) {
  const [phase, setPhase] = useState<"flying" | "landing" | "complete">("flying");

  useEffect(() => {
    // Flying phase
    const flyTimer = setTimeout(() => {
      setPhase("landing");
    }, 2000);

    // Complete phase
    const completeTimer = setTimeout(() => {
      setPhase("complete");
      onComplete();
    }, 3000);

    return () => {
      clearTimeout(flyTimer);
      clearTimeout(completeTimer);
    };
  }, [onComplete]);

  if (phase === "complete") return null;

  return (
    <div
      className={`fixed inset-0 z-[100] bg-white flex items-center justify-center transition-opacity duration-500 ${
        phase === "landing" ? "opacity-0" : "opacity-100"
      }`}
    >
      <div className="relative">
        {/* Animated plane with logo */}
        <div
          className={`transition-all duration-[2000ms] ease-out ${
            phase === "flying"
              ? "translate-x-0 translate-y-0"
              : "-translate-y-[100vh] translate-x-[50vw]"
          }`}
        >
          <div className="flex flex-col items-center gap-4">
            {/* Plane SVG */}
            <svg
              className={`w-24 h-24 text-[#2E7BBF] transition-transform duration-1000 ${
                phase === "landing" ? "rotate-[-45deg]" : ""
              }`}
              viewBox="0 0 24 24"
              fill="currentColor"
            >
              <path d="M21 16v-2l-8-5V3.5c0-.83-.67-1.5-1.5-1.5S10 2.67 10 3.5V9l-8 5v2l8-2.5V19l-2 1.5V22l3.5-1 3.5 1v-1.5L13 19v-5.5l8 2.5z" />
            </svg>
            {/* Logo */}
            <Image
              src="/logo.png"
              alt="Cargo Sales International"
              width={200}
              height={80}
              className="h-16 w-auto"
              priority
            />
            <span className="text-[#2E7BBF] font-bold text-xl">
              Cargo Sales International
            </span>
          </div>
        </div>

        {/* Trail effect */}
        <div
          className={`absolute top-1/2 right-full w-[200vw] h-1 bg-gradient-to-r from-transparent via-[#4A9BA8] to-transparent transition-opacity duration-500 ${
            phase === "flying" ? "opacity-50" : "opacity-0"
          }`}
        />
      </div>
    </div>
  );
}

// Floating CTA Button - always visible
export function FloatingCTA() {
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      setIsVisible(window.scrollY > 300);
    };
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  return (
    <div
      className={`fixed bottom-6 right-6 z-50 transition-all duration-300 ${
        isVisible ? "translate-y-0 opacity-100" : "translate-y-20 opacity-0"
      }`}
    >
      <Link
        href="/contact"
        className="group flex items-center gap-2 bg-[#2E7BBF] text-white px-6 py-4 rounded-full font-bold shadow-lg shadow-[#2E7BBF]/30 hover:bg-[#1E5A8F] hover:shadow-xl transition-all duration-300"
      >
        <svg className="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
          <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z" />
        </svg>
        Book a Shipment
        <svg
          className="w-4 h-4 group-hover:translate-x-1 transition-transform"
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="2"
        >
          <line x1="5" y1="12" x2="19" y2="12" />
          <polyline points="12 5 19 12 12 19" />
        </svg>
      </Link>
    </div>
  );
}

// Navigation Component with dropdowns
export function Navigation() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [servicesOpen, setServicesOpen] = useState(false);

  return (
    <nav className="fixed top-0 left-0 right-0 z-50 bg-white/95 backdrop-blur-md shadow-sm border-b border-slate-100">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Top bar with contact info */}
        <div className="hidden lg:flex justify-end items-center py-2 text-sm border-b border-slate-100">
          <a
            href="tel:+18662872583"
            className="flex items-center gap-2 text-slate-600 hover:text-[#2E7BBF] transition-colors mr-6"
          >
            <svg className="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z" />
            </svg>
            +1 (866) 287-2583
          </a>
          <a
            href="mailto:bookings@cargosalesintl.com"
            className="flex items-center gap-2 text-slate-600 hover:text-[#2E7BBF] transition-colors"
          >
            <svg className="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" />
              <polyline points="22,6 12,13 2,6" />
            </svg>
            bookings@cargosalesintl.com
          </a>
        </div>

        <div className="flex justify-between items-center h-16 lg:h-20">
          {/* Logo */}
          <Link href="/" className="flex items-center gap-3">
            <Image
              src="/logo.png"
              alt="Cargo Sales International"
              width={150}
              height={60}
              className="h-10 w-auto"
              priority
            />
            <div className="hidden sm:flex flex-col">
              <span className="font-bold text-lg text-[#2E7BBF] leading-tight">
                Cargo Sales International
              </span>
              <span className="text-xs text-slate-500 leading-tight">
                Mortuary Transport Since 2000
              </span>
            </div>
          </Link>

          {/* Desktop Navigation */}
          <div className="hidden md:flex items-center gap-8">
            <Link
              href="/"
              className="text-slate-700 hover:text-[#2E7BBF] font-medium transition-colors"
            >
              Home
            </Link>

            {/* Services Dropdown */}
            <div
              className="relative"
              onMouseEnter={() => setServicesOpen(true)}
              onMouseLeave={() => setServicesOpen(false)}
            >
              <button className="flex items-center gap-1 text-slate-700 hover:text-[#2E7BBF] font-medium transition-colors">
                Services
                <svg
                  className={`w-4 h-4 transition-transform ${servicesOpen ? "rotate-180" : ""}`}
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2"
                >
                  <polyline points="6 9 12 15 18 9" />
                </svg>
              </button>

              {servicesOpen && (
                <div className="absolute top-full left-0 mt-2 w-64 bg-white rounded-xl shadow-xl border border-slate-100 py-2 animate-fade-in">
                  <Link
                    href="/services"
                    className="block px-4 py-2 text-slate-700 hover:bg-[#E0F2F5] hover:text-[#2E7BBF] transition-colors"
                  >
                    All Services
                  </Link>
                  <Link
                    href="/services/domestic"
                    className="block px-4 py-2 text-slate-700 hover:bg-[#E0F2F5] hover:text-[#2E7BBF] transition-colors"
                  >
                    Domestic Shipping
                  </Link>
                  <Link
                    href="/services/international"
                    className="block px-4 py-2 text-slate-700 hover:bg-[#E0F2F5] hover:text-[#2E7BBF] transition-colors"
                  >
                    International Repatriation
                  </Link>
                </div>
              )}
            </div>

            <Link
              href="/about"
              className="text-slate-700 hover:text-[#2E7BBF] font-medium transition-colors"
            >
              About Us
            </Link>

            <Link
              href="/contact"
              className="text-slate-700 hover:text-[#2E7BBF] font-medium transition-colors"
            >
              Contact
            </Link>
          </div>

          {/* CTA Button */}
          <div className="hidden md:flex items-center gap-4">
            <Link
              href="/contact"
              className="bg-[#2E7BBF] text-white px-6 py-2.5 rounded-full font-semibold hover:bg-[#1E5A8F] hover:shadow-lg transition-all duration-300"
            >
              Book a Shipment
            </Link>
          </div>

          {/* Mobile Menu Button */}
          <button
            className="md:hidden p-2"
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            aria-label="Toggle menu"
          >
            {mobileMenuOpen ? (
              <svg className="w-6 h-6 text-slate-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <line x1="18" y1="6" x2="6" y2="18" />
                <line x1="6" y1="6" x2="18" y2="18" />
              </svg>
            ) : (
              <svg className="w-6 h-6 text-slate-700" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <line x1="3" y1="12" x2="21" y2="12" />
                <line x1="3" y1="6" x2="21" y2="6" />
                <line x1="3" y1="18" x2="21" y2="18" />
              </svg>
            )}
          </button>
        </div>

        {/* Mobile Menu */}
        {mobileMenuOpen && (
          <div className="md:hidden py-4 border-t border-slate-100">
            <div className="flex flex-col gap-2">
              <Link href="/" className="text-slate-700 hover:text-[#2E7BBF] font-medium py-2" onClick={() => setMobileMenuOpen(false)}>
                Home
              </Link>
              <Link href="/services" className="text-slate-700 hover:text-[#2E7BBF] font-medium py-2" onClick={() => setMobileMenuOpen(false)}>
                Services
              </Link>
              <Link href="/services/domestic" className="text-slate-500 hover:text-[#2E7BBF] pl-4 py-1 text-sm" onClick={() => setMobileMenuOpen(false)}>
                → Domestic Shipping
              </Link>
              <Link href="/services/international" className="text-slate-500 hover:text-[#2E7BBF] pl-4 py-1 text-sm" onClick={() => setMobileMenuOpen(false)}>
                → International Repatriation
              </Link>
              <Link href="/about" className="text-slate-700 hover:text-[#2E7BBF] font-medium py-2" onClick={() => setMobileMenuOpen(false)}>
                About Us
              </Link>
              <Link href="/contact" className="text-slate-700 hover:text-[#2E7BBF] font-medium py-2" onClick={() => setMobileMenuOpen(false)}>
                Contact
              </Link>
              <Link
                href="/contact"
                className="bg-[#2E7BBF] text-white px-6 py-3 rounded-full font-semibold text-center mt-4"
                onClick={() => setMobileMenuOpen(false)}
              >
                Book a Shipment
              </Link>
            </div>
          </div>
        )}
      </div>
    </nav>
  );
}

// Footer Component
export function Footer() {
  return (
    <footer className="bg-[#0c2940] text-white py-16">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid md:grid-cols-4 gap-12 mb-12">
          {/* Brand */}
          <div className="md:col-span-2">
            <div className="flex items-center gap-3 mb-4">
              <Image
                src="/logo.png"
                alt="Cargo Sales International"
                width={150}
                height={60}
                className="h-10 w-auto brightness-0 invert"
              />
              <span className="font-bold text-lg">Cargo Sales International</span>
            </div>
            <p className="text-slate-400 mb-6 max-w-md">
              With more than 24 years of logistics experience dedicated to the
              funeral care industry. We help funeral homes better serve their families
              with a wide range of shipping services.
            </p>
            <div className="space-y-2">
              <a href="tel:+18662872583" className="flex items-center gap-2 text-slate-300 hover:text-white transition-colors">
                <svg className="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z" />
                </svg>
                +1 (866) 287-2583
              </a>
              <a href="mailto:bookings@cargosalesintl.com" className="flex items-center gap-2 text-slate-300 hover:text-white transition-colors">
                <svg className="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" />
                  <polyline points="22,6 12,13 2,6" />
                </svg>
                bookings@cargosalesintl.com
              </a>
            </div>
          </div>

          {/* Quick Links */}
          <div>
            <h4 className="font-semibold mb-4">Quick Links</h4>
            <ul className="space-y-2">
              <li><Link href="/" className="text-slate-400 hover:text-white transition-colors">Home</Link></li>
              <li><Link href="/services" className="text-slate-400 hover:text-white transition-colors">Services</Link></li>
              <li><Link href="/about" className="text-slate-400 hover:text-white transition-colors">About Us</Link></li>
              <li><Link href="/contact" className="text-slate-400 hover:text-white transition-colors">Contact</Link></li>
            </ul>
          </div>

          {/* Services */}
          <div>
            <h4 className="font-semibold mb-4">Services</h4>
            <ul className="space-y-2 text-slate-400">
              <li><Link href="/services/domestic" className="hover:text-white transition-colors">Domestic Shipping</Link></li>
              <li><Link href="/services/international" className="hover:text-white transition-colors">International Repatriation</Link></li>
              <li>Consular Paperwork</li>
              <li>Customs Clearance</li>
            </ul>
          </div>
        </div>

        {/* Bottom Bar */}
        <div className="pt-8 border-t border-slate-800 flex flex-col sm:flex-row justify-between items-center gap-4">
          <p className="text-slate-500 text-sm">
            © {new Date().getFullYear()} Cargo Sales International. All rights reserved.
          </p>
          <div className="flex items-center gap-2 text-slate-400 text-sm">
            <span className="w-2 h-2 bg-green-500 rounded-full animate-pulse" />
            Available 24/7/365
          </div>
        </div>
      </div>
    </footer>
  );
}
