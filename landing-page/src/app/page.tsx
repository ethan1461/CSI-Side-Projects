"use client";

import { useState } from "react";
import Image from "next/image";

// CSI Logo Component
const CSILogo = ({ className = "h-12" }: { className?: string }) => (
  <Image
    src="/logo.svg"
    alt="Cargo Sales International"
    width={120}
    height={48}
    className={className}
    priority
  />
);

// Icons as SVG components
const PlaneIcon = ({ className }: { className?: string }) => (
  <svg
    className={className}
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <path d="M17.8 19.2L16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.5-.1 1 .3 1.3L9 12l-2 3H4l-1 1 3 2 2 3 1-1v-3l3-2 3.5 5.3c.3.4.8.5 1.3.3l.5-.2c.4-.3.6-.7.5-1.2z" />
  </svg>
);

const GlobeIcon = ({ className }: { className?: string }) => (
  <svg
    className={className}
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <circle cx="12" cy="12" r="10" />
    <line x1="2" y1="12" x2="22" y2="12" />
    <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z" />
  </svg>
);

const ClockIcon = ({ className }: { className?: string }) => (
  <svg
    className={className}
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <circle cx="12" cy="12" r="10" />
    <polyline points="12 6 12 12 16 14" />
  </svg>
);

const ShieldIcon = ({ className }: { className?: string }) => (
  <svg
    className={className}
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
    <path d="M9 12l2 2 4-4" />
  </svg>
);

const UsersIcon = ({ className }: { className?: string }) => (
  <svg
    className={className}
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" />
    <circle cx="9" cy="7" r="4" />
    <path d="M23 21v-2a4 4 0 0 0-3-3.87" />
    <path d="M16 3.13a4 4 0 0 1 0 7.75" />
  </svg>
);

const DocumentIcon = ({ className }: { className?: string }) => (
  <svg
    className={className}
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" />
    <polyline points="14 2 14 8 20 8" />
    <line x1="16" y1="13" x2="8" y2="13" />
    <line x1="16" y1="17" x2="8" y2="17" />
    <polyline points="10 9 9 9 8 9" />
  </svg>
);

const TruckIcon = ({ className }: { className?: string }) => (
  <svg
    className={className}
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <rect x="1" y="3" width="15" height="13" />
    <polygon points="16 8 20 8 23 11 23 16 16 16 16 8" />
    <circle cx="5.5" cy="18.5" r="2.5" />
    <circle cx="18.5" cy="18.5" r="2.5" />
  </svg>
);

const CreditCardIcon = ({ className }: { className?: string }) => (
  <svg
    className={className}
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <rect x="1" y="4" width="22" height="16" rx="2" ry="2" />
    <line x1="1" y1="10" x2="23" y2="10" />
  </svg>
);

const CalendarIcon = ({ className }: { className?: string }) => (
  <svg
    className={className}
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <rect x="3" y="4" width="18" height="18" rx="2" ry="2" />
    <line x1="16" y1="2" x2="16" y2="6" />
    <line x1="8" y1="2" x2="8" y2="6" />
    <line x1="3" y1="10" x2="21" y2="10" />
  </svg>
);

const BellIcon = ({ className }: { className?: string }) => (
  <svg
    className={className}
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9" />
    <path d="M13.73 21a2 2 0 0 1-3.46 0" />
  </svg>
);

const PhoneIcon = ({ className }: { className?: string }) => (
  <svg
    className={className}
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z" />
  </svg>
);

const MailIcon = ({ className }: { className?: string }) => (
  <svg
    className={className}
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" />
    <polyline points="22,6 12,13 2,6" />
  </svg>
);

const MapPinIcon = ({ className }: { className?: string }) => (
  <svg
    className={className}
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z" />
    <circle cx="12" cy="10" r="3" />
  </svg>
);

const CheckIcon = ({ className }: { className?: string }) => (
  <svg
    className={className}
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <polyline points="20 6 9 17 4 12" />
  </svg>
);

const MenuIcon = ({ className }: { className?: string }) => (
  <svg
    className={className}
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <line x1="3" y1="12" x2="21" y2="12" />
    <line x1="3" y1="6" x2="21" y2="6" />
    <line x1="3" y1="18" x2="21" y2="18" />
  </svg>
);

const CloseIcon = ({ className }: { className?: string }) => (
  <svg
    className={className}
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <line x1="18" y1="6" x2="6" y2="18" />
    <line x1="6" y1="6" x2="18" y2="18" />
  </svg>
);

const ArrowRightIcon = ({ className }: { className?: string }) => (
  <svg
    className={className}
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <line x1="5" y1="12" x2="19" y2="12" />
    <polyline points="12 5 19 12 12 19" />
  </svg>
);

const HeartIcon = ({ className }: { className?: string }) => (
  <svg
    className={className}
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" />
  </svg>
);

// Navigation Component
function Navigation() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const navLinks = [
    { href: "#services", label: "Services" },
    { href: "#about", label: "About Us" },
    { href: "#why-us", label: "Why Choose Us" },
    { href: "#contact", label: "Contact" },
  ];

  return (
    <nav className="fixed top-0 left-0 right-0 z-50 bg-white/95 backdrop-blur-md shadow-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Top bar with contact info */}
        <div className="hidden lg:flex justify-end items-center py-2 text-sm border-b border-slate-100">
          <a
            href="tel:+18662872583"
            className="flex items-center gap-2 text-slate-600 hover:text-[#4A9BA8] transition-colors mr-6"
          >
            <PhoneIcon className="w-4 h-4" />
            +1 (866) 287-2583
          </a>
          <a
            href="mailto:bookings@cargosalesintl.com"
            className="flex items-center gap-2 text-slate-600 hover:text-[#4A9BA8] transition-colors"
          >
            <MailIcon className="w-4 h-4" />
            bookings@cargosalesintl.com
          </a>
        </div>

        <div className="flex justify-between items-center h-16 lg:h-20">
          {/* Logo */}
          <a href="#" className="flex items-center gap-3">
            <CSILogo className="h-10 w-auto" />
            <div className="hidden sm:flex flex-col">
              <span className="font-bold text-lg text-[#2E7BBF] leading-tight">
                Cargo Sales International
              </span>
              <span className="text-xs text-slate-500 leading-tight">
                Mortuary Transport Since 2000
              </span>
            </div>
          </a>

          {/* Desktop Navigation */}
          <div className="hidden md:flex items-center gap-8">
            {navLinks.map((link) => (
              <a
                key={link.href}
                href={link.href}
                className="text-slate-600 hover:text-[#4A9BA8] font-medium transition-colors"
              >
                {link.label}
              </a>
            ))}
          </div>

          {/* CTA Button */}
          <div className="hidden md:flex items-center gap-4">
            <a
              href="#quote"
              className="bg-gradient-to-r from-[#4A9BA8] to-[#2E7BBF] text-white px-6 py-2.5 rounded-full font-semibold hover:shadow-lg hover:shadow-[#4A9BA8]/25 transition-all duration-300"
            >
              Get a Quote
            </a>
          </div>

          {/* Mobile Menu Button */}
          <button
            className="md:hidden p-2"
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            aria-label="Toggle menu"
          >
            {mobileMenuOpen ? (
              <CloseIcon className="w-6 h-6 text-slate-700" />
            ) : (
              <MenuIcon className="w-6 h-6 text-slate-700" />
            )}
          </button>
        </div>

        {/* Mobile Menu */}
        {mobileMenuOpen && (
          <div className="md:hidden py-4 border-t border-slate-100">
            <div className="flex flex-col gap-4">
              {navLinks.map((link) => (
                <a
                  key={link.href}
                  href={link.href}
                  className="text-slate-600 hover:text-[#4A9BA8] font-medium py-2"
                  onClick={() => setMobileMenuOpen(false)}
                >
                  {link.label}
                </a>
              ))}
              <div className="pt-4 border-t border-slate-100 space-y-2">
                <a
                  href="tel:+18662872583"
                  className="flex items-center gap-2 text-slate-600"
                >
                  <PhoneIcon className="w-4 h-4" />
                  +1 (866) 287-2583
                </a>
                <a
                  href="mailto:bookings@cargosalesintl.com"
                  className="flex items-center gap-2 text-slate-600"
                >
                  <MailIcon className="w-4 h-4" />
                  bookings@cargosalesintl.com
                </a>
              </div>
              <a
                href="#quote"
                className="bg-gradient-to-r from-[#4A9BA8] to-[#2E7BBF] text-white px-6 py-3 rounded-full font-semibold text-center mt-2"
                onClick={() => setMobileMenuOpen(false)}
              >
                Get a Quote
              </a>
            </div>
          </div>
        )}
      </div>
    </nav>
  );
}

// Hero Section
function HeroSection() {
  return (
    <section className="relative min-h-screen gradient-hero overflow-hidden pt-24 lg:pt-32">
      {/* Background Elements */}
      <div className="absolute inset-0 overflow-hidden">
        <div className="absolute top-20 left-10 w-32 h-16 bg-white/5 rounded-full blur-xl" />
        <div className="absolute top-40 right-20 w-48 h-20 bg-white/5 rounded-full blur-xl" />
        <div className="absolute bottom-40 left-1/4 w-40 h-16 bg-white/5 rounded-full blur-xl" />

        {/* Grid pattern */}
        <div
          className="absolute inset-0 opacity-5"
          style={{
            backgroundImage: `url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.4'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E")`,
          }}
        />
      </div>

      <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 lg:py-24">
        <div className="grid lg:grid-cols-2 gap-12 items-center">
          {/* Left Content */}
          <div className="text-center lg:text-left">
            {/* Badge */}
            <div className="inline-flex items-center gap-2 bg-white/10 backdrop-blur-sm border border-white/20 rounded-full px-4 py-2 mb-6">
              <HeartIcon className="w-4 h-4 text-pink-300" />
              <span className="text-white/90 text-sm font-medium">
                100% Female Owned & Operated Since 2000
              </span>
            </div>

            <h1 className="text-4xl sm:text-5xl lg:text-6xl font-bold text-white leading-tight mb-6">
              Human Remains{" "}
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-[#6BB5C0] to-[#4A95D9]">
                Transport Services
              </span>
            </h1>

            <p className="text-lg sm:text-xl text-white/80 mb-4 max-w-xl mx-auto lg:mx-0">
              Serving the funeral care industry for over 24 years.
            </p>

            <p className="text-base text-white/70 mb-8 max-w-xl mx-auto lg:mx-0">
              Let Cargo Sales International do the work, leaving you more time
              to take care of your clients. We are at your service 24/7.
            </p>

            {/* CTA Buttons */}
            <div className="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start mb-12">
              <a
                href="#quote"
                className="group bg-white text-[#2E7BBF] px-8 py-4 rounded-full font-bold text-lg hover:shadow-xl hover:shadow-white/25 transition-all duration-300 flex items-center justify-center gap-2"
              >
                Get a Quote
                <ArrowRightIcon className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
              </a>
              <a
                href="tel:+18662872583"
                className="group glass text-white px-8 py-4 rounded-full font-semibold text-lg hover:bg-white/20 transition-all duration-300 flex items-center justify-center gap-2"
              >
                <PhoneIcon className="w-5 h-5" />
                Call Us Now
              </a>
            </div>

            {/* Trust Indicators */}
            <div className="flex flex-wrap justify-center lg:justify-start gap-6 text-white/70 text-sm">
              <div className="flex items-center gap-2">
                <CheckIcon className="w-5 h-5 text-[#6BB5C0]" />
                <span>NO Booking Fees</span>
              </div>
              <div className="flex items-center gap-2">
                <CheckIcon className="w-5 h-5 text-[#6BB5C0]" />
                <span>24/7 Support</span>
              </div>
              <div className="flex items-center gap-2">
                <CheckIcon className="w-5 h-5 text-[#6BB5C0]" />
                <span>We Are Not a Call Center</span>
              </div>
            </div>
          </div>

          {/* Right Content - Stats Card */}
          <div className="relative">
            <div className="glass rounded-3xl p-8 lg:p-10">
              <h3 className="text-white text-xl font-semibold mb-8 text-center">
                Trusted by Funeral Homes Nationwide
              </h3>

              <div className="grid grid-cols-2 gap-6">
                <div className="text-center">
                  <div className="text-4xl lg:text-5xl font-bold text-[#6BB5C0] mb-2">
                    100k+
                  </div>
                  <div className="text-white/70 text-sm">Cases Safely Shipped</div>
                </div>
                <div className="text-center">
                  <div className="text-4xl lg:text-5xl font-bold text-[#6BB5C0] mb-2">
                    24+
                  </div>
                  <div className="text-white/70 text-sm">Years of Experience</div>
                </div>
                <div className="text-center">
                  <div className="text-4xl lg:text-5xl font-bold text-[#6BB5C0] mb-2">
                    24/7
                  </div>
                  <div className="text-white/70 text-sm">Immediate Attention</div>
                </div>
                <div className="text-center">
                  <div className="text-4xl lg:text-5xl font-bold text-[#6BB5C0] mb-2">
                    $0
                  </div>
                  <div className="text-white/70 text-sm">Additional Costs</div>
                </div>
              </div>
            </div>

            {/* IATA Badge - below stats card */}
            <div className="mt-6 bg-white/10 backdrop-blur-sm border border-white/20 rounded-2xl p-4">
              <div className="flex items-center justify-center gap-3">
                <div className="w-10 h-10 bg-white rounded-full flex items-center justify-center">
                  <ShieldIcon className="w-5 h-5 text-[#2E7BBF]" />
                </div>
                <div>
                  <div className="font-semibold text-white">IATA Certified</div>
                  <div className="text-xs text-white/70">CNS - An IATA Company</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Bottom Wave */}
      <div className="absolute bottom-0 left-0 right-0">
        <svg viewBox="0 0 1440 120" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path
            d="M0 120L48 110C96 100 192 80 288 70C384 60 480 60 576 65C672 70 768 80 864 85C960 90 1056 90 1152 85C1248 80 1344 70 1392 65L1440 60V120H1392C1344 120 1248 120 1152 120C1056 120 960 120 864 120C768 120 672 120 576 120C480 120 384 120 288 120C192 120 96 120 48 120H0Z"
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
      icon: GlobeIcon,
      title: "International & Domestic Shipping",
      description:
        "Simplify your logistics needs with our versatile shipping options, enabling smooth and secure transportation both internationally and domestically.",
    },
    {
      icon: CalendarIcon,
      title: "Confirmed Itineraries",
      description:
        "We ensure peace of mind with our meticulously confirmed itineraries, assuring you of precise and reliable scheduling for seamless transportation.",
    },
    {
      icon: TruckIcon,
      title: "Local Pick-ups & Deliveries",
      description:
        "Pick-up and delivery services from local funeral homes in Miami, Houston, Los Angeles, New York and Washington DC.",
    },
    {
      icon: CreditCardIcon,
      title: "Prepaid Flight Charges",
      description:
        "All shipments are prepaid on our account, eliminating the necessity to bring payments to the airport.",
    },
    {
      icon: DocumentIcon,
      title: "Consular Paperwork",
      description:
        "We facilitate translations, apostilles, and legalization of international paperwork for consular clearance.",
    },
    {
      icon: ShieldIcon,
      title: "Customs Clearance",
      description:
        "Trust us to handle the intricacies of customs procedures, ensuring a hassle-free experience as we expertly navigate international regulations.",
    },
    {
      icon: BellIcon,
      title: "Cancellation & Delay Updates",
      description:
        "We prioritize clear communication, keeping you updated and well-informed about any potential cancellations or delays.",
    },
  ];

  return (
    <section id="services" className="py-20 lg:py-32 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Section Header */}
        <div className="text-center max-w-3xl mx-auto mb-16">
          <div className="inline-flex items-center gap-2 bg-[#E0F2F5] text-[#3A8592] rounded-full px-4 py-2 text-sm font-medium mb-4">
            <PlaneIcon className="w-4 h-4" />
            Our Services
          </div>
          <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold text-slate-900 mb-6">
            Services for{" "}
            <span className="text-[#4A9BA8]">Funeral Homes</span>
          </h2>
          <p className="text-lg text-slate-600">
            Our team of highly trained and multilingual specialized professionals
            are ready to assist you with all the arrangements and logistics
            necessary for your Domestic and International shipments.
          </p>
        </div>

        {/* Services Grid */}
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
          {services.map((service, index) => (
            <div
              key={index}
              className="group relative bg-white border border-slate-200 rounded-2xl p-6 hover:shadow-xl hover:shadow-slate-200/50 hover:border-[#4A9BA8]/20 transition-all duration-300"
            >
              {/* Icon */}
              <div className="w-14 h-14 bg-gradient-to-br from-[#4A9BA8] to-[#2E7BBF] rounded-xl flex items-center justify-center mb-5 group-hover:scale-110 transition-transform duration-300">
                <service.icon className="w-7 h-7 text-white" />
              </div>

              <h3 className="text-lg font-bold text-slate-900 mb-3">
                {service.title}
              </h3>
              <p className="text-slate-600 text-sm">{service.description}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

// About Section
function AboutSection() {
  return (
    <section id="about" className="py-20 lg:py-32 bg-slate-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid lg:grid-cols-2 gap-12 items-center">
          {/* Left Content */}
          <div>
            <div className="inline-flex items-center gap-2 bg-[#E0F2F5] text-[#3A8592] rounded-full px-4 py-2 text-sm font-medium mb-4">
              <UsersIcon className="w-4 h-4" />
              About Us
            </div>
            <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold text-slate-900 mb-6">
              We Are{" "}
              <span className="text-[#4A9BA8]">Not a Call Center</span>
            </h2>
            <p className="text-lg text-slate-600 mb-6">
              At Cargo Sales International, we take great pride in offering
              exceptional service and customer support. Whether you require a
              price quote, assistance with crafting an itinerary, or any
              information, we are here to help.
            </p>
            <p className="text-slate-600 mb-8">
              We&apos;re a team of highly trained professionals who have been
              serving the funeral care industry for over 24 years. We&apos;re
              committed to bringing you top niche assistance and expertise.
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
              ].map((feature, idx) => (
                <div key={idx} className="flex items-center gap-2">
                  <CheckIcon className="w-5 h-5 text-[#4A9BA8]" />
                  <span className="text-slate-700">{feature}</span>
                </div>
              ))}
            </div>
          </div>

          {/* Right Content */}
          <div className="relative">
            <div className="bg-white rounded-3xl p-8 shadow-xl">
              <div className="text-center mb-8">
                <div className="inline-flex items-center justify-center w-20 h-20 bg-gradient-to-br from-[#4A9BA8] to-[#2E7BBF] rounded-full mb-4">
                  <HeartIcon className="w-10 h-10 text-white" />
                </div>
                <h3 className="text-2xl font-bold text-slate-900 mb-2">
                  100% Female Owned & Operated
                </h3>
                <p className="text-slate-600">For the past 24 years</p>
              </div>

              <div className="space-y-4">
                <div className="bg-slate-50 rounded-xl p-4">
                  <p className="text-slate-700 italic">
                    &ldquo;We serve our multi-cultured clientele with a wide range
                    of shipping services custom fit to your needs.&rdquo;
                  </p>
                </div>
                <p className="text-sm text-slate-600 text-center">
                  We have strategic alliances with numerous airlines worldwide
                  which enable us to offer you the best routing at the most
                  affordable prices.
                </p>
              </div>
            </div>

            {/* Decorative element */}
            <div className="absolute -z-10 top-4 left-4 w-full h-full bg-gradient-to-br from-[#4A9BA8]/20 to-[#2E7BBF]/20 rounded-3xl" />
          </div>
        </div>
      </div>
    </section>
  );
}

// Why Choose Us Section
function WhyChooseUsSection() {
  const reasons = [
    {
      number: "100k+",
      label: "Cases Safely Shipped",
      description:
        "Trust our expertise and experience for secure and reliable transportation.",
      icon: PlaneIcon,
    },
    {
      number: "24+",
      label: "Years of Logistics Experience",
      description:
        "Rely on our extensive network, proven track record, and airline relationships in delivering excellent servicing, pricing, and customer support.",
      icon: ClockIcon,
    },
    {
      number: "24/7",
      label: "We Are Not a Call Center",
      description:
        "Rest assured knowing that our dedicated team is available around the clock to provide prompt and attentive assistance whenever you need it.",
      icon: UsersIcon,
    },
  ];

  return (
    <section id="why-us" className="py-20 lg:py-32 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Section Header */}
        <div className="text-center max-w-3xl mx-auto mb-16">
          <div className="inline-flex items-center gap-2 bg-[#E0F2F5] text-[#3A8592] rounded-full px-4 py-2 text-sm font-medium mb-4">
            <ShieldIcon className="w-4 h-4" />
            Why Choose Us
          </div>
          <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold text-slate-900 mb-6">
            We Provide an{" "}
            <span className="text-[#4A9BA8]">Extraordinary Experience</span>
          </h2>
        </div>

        {/* Stats Grid */}
        <div className="grid md:grid-cols-3 gap-8">
          {reasons.map((item, index) => (
            <div
              key={index}
              className="relative bg-gradient-to-br from-slate-50 to-white rounded-3xl p-8 border border-slate-100 hover:shadow-xl transition-shadow duration-300"
            >
              <div className="w-14 h-14 bg-gradient-to-br from-[#4A9BA8] to-[#2E7BBF] rounded-xl flex items-center justify-center mb-6">
                <item.icon className="w-7 h-7 text-white" />
              </div>

              <div className="text-5xl font-bold text-[#2E7BBF] mb-2">
                {item.number}
              </div>
              <h3 className="text-xl font-bold text-slate-900 mb-3">
                {item.label}
              </h3>
              <p className="text-slate-600">{item.description}</p>
            </div>
          ))}
        </div>

        {/* Trust Badges */}
        <div className="mt-16 text-center">
          <p className="text-sm text-slate-500 mb-6">Certified & Recognized By</p>
          <div className="flex flex-wrap justify-center items-center gap-8">
            <div className="flex items-center gap-2 text-slate-600">
              <ShieldIcon className="w-6 h-6 text-[#4A9BA8]" />
              <span className="font-medium">U.S. Department of Homeland Security</span>
            </div>
            <div className="flex items-center gap-2 text-slate-600">
              <GlobeIcon className="w-6 h-6 text-[#4A9BA8]" />
              <span className="font-medium">CNS - An IATA Company</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

// Quote Form Section
function QuoteFormSection() {
  return (
    <section id="quote" className="py-20 lg:py-32 gradient-cta relative overflow-hidden">
      {/* Background elements */}
      <div className="absolute inset-0 overflow-hidden">
        <div className="absolute top-10 left-10 w-64 h-64 bg-white/5 rounded-full blur-3xl" />
        <div className="absolute bottom-10 right-10 w-96 h-96 bg-[#2E7BBF]/10 rounded-full blur-3xl" />
      </div>

      <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid lg:grid-cols-2 gap-12 items-center">
          {/* Left Content */}
          <div className="text-center lg:text-left">
            <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold text-white mb-6">
              Start Your{" "}
              <span className="text-[#B5DEE5]">Quote Today</span>
            </h2>
            <p className="text-lg text-white/80 mb-8">
              We simplify & streamline the booking process for funeral homes on
              all domestic & international shipments, enabling the funeral
              director and staff to have more time to assist the family.
            </p>

            {/* Contact Options */}
            <div className="space-y-4 mb-8">
              <a
                href="tel:+18662872583"
                className="flex items-center justify-center lg:justify-start gap-3 text-white hover:text-[#B5DEE5] transition-colors"
              >
                <div className="w-12 h-12 bg-white/10 rounded-full flex items-center justify-center">
                  <PhoneIcon className="w-5 h-5" />
                </div>
                <div className="text-left">
                  <div className="text-sm text-white/60">Call Us</div>
                  <div className="font-semibold">+1 (866) 287-2583</div>
                </div>
              </a>
              <a
                href="mailto:bookings@cargosalesintl.com"
                className="flex items-center justify-center lg:justify-start gap-3 text-white hover:text-[#B5DEE5] transition-colors"
              >
                <div className="w-12 h-12 bg-white/10 rounded-full flex items-center justify-center">
                  <MailIcon className="w-5 h-5" />
                </div>
                <div className="text-left">
                  <div className="text-sm text-white/60">Email Us</div>
                  <div className="font-semibold">bookings@cargosalesintl.com</div>
                </div>
              </a>
            </div>

            {/* Available badge */}
            <div className="inline-flex items-center gap-2 bg-white/10 backdrop-blur-sm border border-white/20 rounded-full px-4 py-2">
              <span className="w-2 h-2 bg-green-400 rounded-full animate-pulse" />
              <span className="text-white/90 text-sm">
                Live team available 24/7/365
              </span>
            </div>
          </div>

          {/* Right Content - Quote Form */}
          <div className="bg-white rounded-3xl p-8 shadow-2xl">
            <h3 className="text-2xl font-bold text-slate-900 mb-6">
              Request a Quote
            </h3>
            <form className="space-y-4">
              <div className="grid sm:grid-cols-2 gap-4">
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">
                    Airport of Origin
                  </label>
                  <input
                    type="text"
                    className="w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-[#4A9BA8] focus:ring-2 focus:ring-[#E0F2F5] outline-none transition-all"
                    placeholder="e.g., MIA"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">
                    Airport of Destination
                  </label>
                  <input
                    type="text"
                    className="w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-[#4A9BA8] focus:ring-2 focus:ring-[#E0F2F5] outline-none transition-all"
                    placeholder="e.g., LAX"
                  />
                </div>
              </div>
              <div className="grid sm:grid-cols-2 gap-4">
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">
                    Flight Date
                  </label>
                  <input
                    type="date"
                    className="w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-[#4A9BA8] focus:ring-2 focus:ring-[#E0F2F5] outline-none transition-all"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">
                    Weight (lbs)
                  </label>
                  <input
                    type="number"
                    className="w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-[#4A9BA8] focus:ring-2 focus:ring-[#E0F2F5] outline-none transition-all"
                    placeholder="Enter weight"
                  />
                </div>
              </div>
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1">
                  Funeral Home Name
                </label>
                <input
                  type="text"
                  className="w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-[#4A9BA8] focus:ring-2 focus:ring-[#E0F2F5] outline-none transition-all"
                  placeholder="Your funeral home name"
                />
              </div>
              <div className="grid sm:grid-cols-2 gap-4">
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">
                    Email
                  </label>
                  <input
                    type="email"
                    className="w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-[#4A9BA8] focus:ring-2 focus:ring-[#E0F2F5] outline-none transition-all"
                    placeholder="your@email.com"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">
                    Phone
                  </label>
                  <input
                    type="tel"
                    className="w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-[#4A9BA8] focus:ring-2 focus:ring-[#E0F2F5] outline-none transition-all"
                    placeholder="(555) 123-4567"
                  />
                </div>
              </div>
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1">
                  Comments (optional)
                </label>
                <textarea
                  rows={3}
                  className="w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-[#4A9BA8] focus:ring-2 focus:ring-[#E0F2F5] outline-none transition-all resize-none"
                  placeholder="Any additional information..."
                />
              </div>
              <button
                type="submit"
                className="w-full bg-gradient-to-r from-[#4A9BA8] to-[#2E7BBF] text-white py-4 rounded-xl font-semibold text-lg hover:shadow-lg hover:shadow-[#4A9BA8]/25 transition-all duration-300 flex items-center justify-center gap-2"
              >
                Submit Quote Request
                <ArrowRightIcon className="w-5 h-5" />
              </button>
            </form>
          </div>
        </div>
      </div>
    </section>
  );
}

// Contact Section
function ContactSection() {
  return (
    <section id="contact" className="py-20 lg:py-32 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center max-w-3xl mx-auto mb-16">
          <div className="inline-flex items-center gap-2 bg-[#E0F2F5] text-[#3A8592] rounded-full px-4 py-2 text-sm font-medium mb-4">
            <MapPinIcon className="w-4 h-4" />
            Contact Us
          </div>
          <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold text-slate-900 mb-6">
            Should You Have Any{" "}
            <span className="text-[#4A9BA8]">Questions or Concerns</span>
          </h2>
          <p className="text-lg text-slate-600">
            Our team is ready to assist you - reach out to us anytime.
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-8">
          {/* Call Us */}
          <a
            href="tel:+18662872583"
            className="group bg-white border border-slate-200 rounded-2xl p-8 text-center hover:shadow-xl hover:border-[#4A9BA8]/20 transition-all duration-300"
          >
            <div className="w-16 h-16 bg-gradient-to-br from-[#4A9BA8] to-[#2E7BBF] rounded-full flex items-center justify-center mx-auto mb-4 group-hover:scale-110 transition-transform">
              <PhoneIcon className="w-7 h-7 text-white" />
            </div>
            <h3 className="text-xl font-bold text-slate-900 mb-2">Call Us</h3>
            <p className="text-[#4A9BA8] font-semibold">+1 (866) 287-2583</p>
          </a>

          {/* Email Us */}
          <a
            href="mailto:bookings@cargosalesintl.com"
            className="group bg-white border border-slate-200 rounded-2xl p-8 text-center hover:shadow-xl hover:border-[#4A9BA8]/20 transition-all duration-300"
          >
            <div className="w-16 h-16 bg-gradient-to-br from-[#4A9BA8] to-[#2E7BBF] rounded-full flex items-center justify-center mx-auto mb-4 group-hover:scale-110 transition-transform">
              <MailIcon className="w-7 h-7 text-white" />
            </div>
            <h3 className="text-xl font-bold text-slate-900 mb-2">Email Us</h3>
            <p className="text-[#4A9BA8] font-semibold">bookings@cargosalesintl.com</p>
          </a>

          {/* Find Us */}
          <div className="bg-white border border-slate-200 rounded-2xl p-8 text-center">
            <div className="w-16 h-16 bg-gradient-to-br from-[#4A9BA8] to-[#2E7BBF] rounded-full flex items-center justify-center mx-auto mb-4">
              <MapPinIcon className="w-7 h-7 text-white" />
            </div>
            <h3 className="text-xl font-bold text-slate-900 mb-2">Find Us</h3>
            <p className="text-slate-600 text-sm">
              8200 NW 41st Street, Suite 200
              <br />
              Doral, FL 33166
            </p>
            <p className="text-slate-600 text-sm mt-2">
              3350 SW 148th Avenue, Suite 110
              <br />
              Miramar, FL 33027
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}

// Footer
function Footer() {
  return (
    <footer className="bg-[#0c2940] text-white py-16">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid md:grid-cols-4 gap-12 mb-12">
          {/* Brand */}
          <div className="md:col-span-2">
            <div className="flex items-center gap-3 mb-4">
              <CSILogo className="h-10 w-auto brightness-0 invert" />
              <span className="font-bold text-lg">Cargo Sales International</span>
            </div>
            <p className="text-slate-400 mb-6 max-w-md">
              With more than 24 years of logistics experience dedicated to the
              funeral care industry. We serve our multi-cultured clients with a
              wide range of shipping services.
            </p>
            <div className="space-y-2">
              <a
                href="tel:+18662872583"
                className="flex items-center gap-2 text-slate-300 hover:text-white transition-colors"
              >
                <PhoneIcon className="w-4 h-4" />
                +1 (866) 287-2583
              </a>
              <a
                href="mailto:bookings@cargosalesintl.com"
                className="flex items-center gap-2 text-slate-300 hover:text-white transition-colors"
              >
                <MailIcon className="w-4 h-4" />
                bookings@cargosalesintl.com
              </a>
              <div className="flex items-start gap-2 text-slate-300">
                <MapPinIcon className="w-4 h-4 mt-1 flex-shrink-0" />
                <div>
                  <p>8200 NW 41st Street, Suite 200, Doral, FL 33166</p>
                  <p>3350 SW 148th Avenue, Suite 110, Miramar, FL 33027</p>
                </div>
              </div>
            </div>
          </div>

          {/* Quick Links */}
          <div>
            <h4 className="font-semibold mb-4">Information</h4>
            <ul className="space-y-2">
              <li>
                <a href="#" className="text-slate-400 hover:text-white transition-colors">
                  Home
                </a>
              </li>
              <li>
                <a href="#services" className="text-slate-400 hover:text-white transition-colors">
                  Services
                </a>
              </li>
              <li>
                <a href="#about" className="text-slate-400 hover:text-white transition-colors">
                  About Us
                </a>
              </li>
              <li>
                <a href="#quote" className="text-slate-400 hover:text-white transition-colors">
                  Get a Quote
                </a>
              </li>
              <li>
                <a href="#contact" className="text-slate-400 hover:text-white transition-colors">
                  Contact Us
                </a>
              </li>
            </ul>
          </div>

          {/* Services */}
          <div>
            <h4 className="font-semibold mb-4">Services</h4>
            <ul className="space-y-2 text-slate-400">
              <li>International Shipping</li>
              <li>Domestic Shipping</li>
              <li>Consular Paperwork</li>
              <li>Customs Clearance</li>
              <li>Local Pick-ups & Deliveries</li>
            </ul>
          </div>
        </div>

        {/* Bottom Bar */}
        <div className="pt-8 border-t border-slate-800 flex flex-col sm:flex-row justify-between items-center gap-4">
          <p className="text-slate-500 text-sm">
            &copy; {new Date().getFullYear()} Cargo Sales International. All
            rights reserved.
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

// Main Page Component
export default function Home() {
  return (
    <main className="min-h-screen">
      <Navigation />
      <HeroSection />
      <ServicesSection />
      <AboutSection />
      <WhyChooseUsSection />
      <QuoteFormSection />
      <ContactSection />
      <Footer />
    </main>
  );
}
