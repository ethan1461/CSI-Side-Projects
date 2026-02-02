"use client";

import { useState } from "react";

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

const DollarIcon = ({ className }: { className?: string }) => (
  <svg
    className={className}
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <line x1="12" y1="1" x2="12" y2="23" />
    <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6" />
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

const RouteIcon = ({ className }: { className?: string }) => (
  <svg
    className={className}
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
  >
    <circle cx="6" cy="19" r="3" />
    <path d="M9 19h8.5a3.5 3.5 0 0 0 0-7h-11a3.5 3.5 0 0 1 0-7H15" />
    <circle cx="18" cy="5" r="3" />
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

// Navigation Component
function Navigation() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  const navLinks = [
    { href: "#services", label: "Services" },
    { href: "#why-csi", label: "Why CSI" },
    { href: "#how-it-works", label: "How It Works" },
    { href: "#contact", label: "Contact" },
  ];

  return (
    <nav className="fixed top-0 left-0 right-0 z-50 bg-white/95 backdrop-blur-md shadow-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16 lg:h-20">
          {/* Logo */}
          <div className="flex items-center gap-2">
            <div className="w-10 h-10 rounded-full bg-gradient-to-br from-[#1a4a82] to-[#0ea5e9] flex items-center justify-center">
              <PlaneIcon className="w-5 h-5 text-white" />
            </div>
            <div className="flex flex-col">
              <span className="font-bold text-lg text-[#0f2744] leading-tight">
                CSI
              </span>
              <span className="text-[10px] text-slate-500 leading-tight hidden sm:block">
                Cargo Sales International
              </span>
            </div>
          </div>

          {/* Desktop Navigation */}
          <div className="hidden md:flex items-center gap-8">
            {navLinks.map((link) => (
              <a
                key={link.href}
                href={link.href}
                className="text-slate-600 hover:text-[#1a4a82] font-medium transition-colors"
              >
                {link.label}
              </a>
            ))}
          </div>

          {/* CTA Button */}
          <div className="hidden md:flex items-center gap-4">
            <a
              href="tel:+1-800-CSI-SHIP"
              className="text-slate-600 hover:text-[#1a4a82] font-medium flex items-center gap-2"
            >
              <PhoneIcon className="w-4 h-4" />
              <span>1-800-CSI-SHIP</span>
            </a>
            <a
              href="#contact"
              className="bg-gradient-to-r from-[#1a4a82] to-[#0ea5e9] text-white px-6 py-2.5 rounded-full font-semibold hover:shadow-lg hover:shadow-[#1a4a82]/25 transition-all duration-300"
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
                  className="text-slate-600 hover:text-[#1a4a82] font-medium py-2"
                  onClick={() => setMobileMenuOpen(false)}
                >
                  {link.label}
                </a>
              ))}
              <a
                href="#contact"
                className="bg-gradient-to-r from-[#1a4a82] to-[#0ea5e9] text-white px-6 py-3 rounded-full font-semibold text-center mt-2"
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
    <section className="relative min-h-screen gradient-hero overflow-hidden pt-16 lg:pt-20">
      {/* Animated Background Elements */}
      <div className="absolute inset-0 overflow-hidden">
        {/* Clouds */}
        <div className="absolute top-20 left-10 w-32 h-16 bg-white/5 rounded-full blur-xl" />
        <div className="absolute top-40 right-20 w-48 h-20 bg-white/5 rounded-full blur-xl" />
        <div className="absolute bottom-40 left-1/4 w-40 h-16 bg-white/5 rounded-full blur-xl" />

        {/* Grid pattern */}
        <div
          className="absolute inset-0 opacity-10"
          style={{
            backgroundImage: `url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.4'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E")`,
          }}
        />

        {/* Animated plane */}
        <div className="animate-plane-fly absolute top-1/3">
          <PlaneIcon className="w-12 h-12 text-white/20" />
        </div>
      </div>

      <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 lg:py-32">
        <div className="grid lg:grid-cols-2 gap-12 items-center">
          {/* Left Content */}
          <div className="text-center lg:text-left">
            {/* Badge */}
            <div className="inline-flex items-center gap-2 bg-white/10 backdrop-blur-sm border border-white/20 rounded-full px-4 py-2 mb-6">
              <span className="w-2 h-2 bg-green-400 rounded-full animate-pulse" />
              <span className="text-white/90 text-sm font-medium">
                24/7 Live Support Available
              </span>
            </div>

            <h1 className="text-4xl sm:text-5xl lg:text-6xl font-bold text-white leading-tight mb-6">
              End-to-End{" "}
              <span className="text-transparent bg-clip-text bg-gradient-to-r from-[#38bdf8] to-[#7dd3fc]">
                Air Cargo
              </span>{" "}
              Logistics for Human Remains
            </h1>

            <p className="text-lg sm:text-xl text-white/80 mb-8 max-w-xl mx-auto lg:mx-0">
              Trusted by funeral homes nationwide. We handle every detail from
              booking to delivery, with{" "}
              <span className="text-[#38bdf8] font-semibold">
                complete transparency
              </span>{" "}
              and zero booking fees.
            </p>

            {/* CTA Buttons */}
            <div className="flex flex-col sm:flex-row gap-4 justify-center lg:justify-start mb-12">
              <a
                href="#contact"
                className="group bg-white text-[#1a4a82] px-8 py-4 rounded-full font-bold text-lg hover:shadow-xl hover:shadow-white/25 transition-all duration-300 flex items-center justify-center gap-2"
              >
                Get Started Free
                <ArrowRightIcon className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
              </a>
              <a
                href="#how-it-works"
                className="group glass text-white px-8 py-4 rounded-full font-semibold text-lg hover:bg-white/20 transition-all duration-300 flex items-center justify-center gap-2"
              >
                See How It Works
              </a>
            </div>

            {/* Trust Indicators */}
            <div className="flex flex-wrap justify-center lg:justify-start gap-6 text-white/70 text-sm">
              <div className="flex items-center gap-2">
                <CheckIcon className="w-5 h-5 text-green-400" />
                <span>Completely FREE Service</span>
              </div>
              <div className="flex items-center gap-2">
                <CheckIcon className="w-5 h-5 text-green-400" />
                <span>5-6 Routing Options</span>
              </div>
              <div className="flex items-center gap-2">
                <CheckIcon className="w-5 h-5 text-green-400" />
                <span>International Expertise</span>
              </div>
            </div>
          </div>

          {/* Right Content - Stats Card */}
          <div className="relative">
            <div className="glass rounded-3xl p-8 lg:p-10">
              <h3 className="text-white text-xl font-semibold mb-8">
                Why Funeral Directors Trust CSI
              </h3>

              <div className="grid grid-cols-2 gap-6">
                <div className="text-center">
                  <div className="text-4xl lg:text-5xl font-bold text-[#38bdf8] mb-2">
                    24/7
                  </div>
                  <div className="text-white/70 text-sm">Live Agents</div>
                </div>
                <div className="text-center">
                  <div className="text-4xl lg:text-5xl font-bold text-[#38bdf8] mb-2">
                    5-6
                  </div>
                  <div className="text-white/70 text-sm">Routing Options</div>
                </div>
                <div className="text-center">
                  <div className="text-4xl lg:text-5xl font-bold text-[#38bdf8] mb-2">
                    $0
                  </div>
                  <div className="text-white/70 text-sm">Booking Fees</div>
                </div>
                <div className="text-center">
                  <div className="text-4xl lg:text-5xl font-bold text-[#38bdf8] mb-2">
                    1hr
                  </div>
                  <div className="text-white/70 text-sm">Response Time</div>
                </div>
              </div>

              {/* Floating Plane Icon */}
              <div className="absolute -top-6 -right-6 w-16 h-16 bg-gradient-to-br from-[#f59e0b] to-[#fbbf24] rounded-2xl flex items-center justify-center shadow-lg animate-float">
                <PlaneIcon className="w-8 h-8 text-white" />
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Bottom Wave */}
      <div className="absolute bottom-0 left-0 right-0">
        <svg
          viewBox="0 0 1440 120"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
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
      icon: PlaneIcon,
      title: "Domestic Air Freight",
      description:
        "Seamless coordination with all major carriers for reliable domestic shipments. Same published rates as calling airlines directly.",
      features: [
        "Multiple routing options",
        "Cargo acceptance coordination",
        "Real-time tracking",
      ],
    },
    {
      icon: GlobeIcon,
      title: "International Repatriation",
      description:
        "Expert handling of complex international shipments with full documentation support and consulate processing.",
      features: [
        "Consulate liaison",
        "Translation services",
        "Apostille processing",
      ],
    },
    {
      icon: DocumentIcon,
      title: "Documentation Management",
      description:
        "Complete paperwork handling including permits, certificates, and country-specific requirements. No detail overlooked.",
      features: [
        "Permit coordination",
        "Document validation",
        "Compliance assurance",
      ],
    },
    {
      icon: RouteIcon,
      title: "Route Optimization",
      description:
        "5-6 routing options per shipment, optimized for reliability, timing, and cost. Never limited to a single carrier.",
      features: [
        "Multi-carrier access",
        "SLA-based selection",
        "Contingency planning",
      ],
    },
  ];

  return (
    <section id="services" className="py-20 lg:py-32 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Section Header */}
        <div className="text-center max-w-3xl mx-auto mb-16">
          <div className="inline-flex items-center gap-2 bg-[#dbeafe] text-[#1a4a82] rounded-full px-4 py-2 text-sm font-medium mb-4">
            <PlaneIcon className="w-4 h-4" />
            Our Services
          </div>
          <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold text-slate-900 mb-6">
            Complete Air Cargo{" "}
            <span className="text-[#1a4a82]">Logistics Solutions</span>
          </h2>
          <p className="text-lg text-slate-600">
            From initial booking to final delivery, we orchestrate every aspect
            of human remains transportation with precision and care.
          </p>
        </div>

        {/* Services Grid */}
        <div className="grid md:grid-cols-2 gap-8">
          {services.map((service, index) => (
            <div
              key={index}
              className="group relative bg-white border border-slate-200 rounded-2xl p-8 hover:shadow-xl hover:shadow-slate-200/50 hover:border-[#1a4a82]/20 transition-all duration-300"
            >
              {/* Icon */}
              <div className="w-14 h-14 bg-gradient-to-br from-[#1a4a82] to-[#0ea5e9] rounded-xl flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
                <service.icon className="w-7 h-7 text-white" />
              </div>

              <h3 className="text-xl font-bold text-slate-900 mb-3">
                {service.title}
              </h3>
              <p className="text-slate-600 mb-6">{service.description}</p>

              {/* Features */}
              <ul className="space-y-2">
                {service.features.map((feature, idx) => (
                  <li key={idx} className="flex items-center gap-2 text-sm">
                    <CheckIcon className="w-4 h-4 text-[#0ea5e9]" />
                    <span className="text-slate-600">{feature}</span>
                  </li>
                ))}
              </ul>

              {/* Hover decoration */}
              <div className="absolute top-0 right-0 w-20 h-20 bg-gradient-to-br from-[#dbeafe] to-transparent rounded-bl-[100px] opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

// Why CSI Section (The CSI Difference)
function WhyCSISection() {
  const advantages = [
    {
      icon: DollarIcon,
      title: "Cost",
      subtitle: "Completely FREE Service",
      description:
        "Pay the same published airline rate as calling the carrier directly. No hidden booking fees, no surprises. We earn through carrier partnerships, not by charging you more.",
      highlight: "$0 Booking Fees",
    },
    {
      icon: ClockIcon,
      title: "Convenience",
      subtitle: "All-in-One Partner",
      description:
        "24/7/365 live agents (not call centers) with 30-60 minute response times. We handle routing, documentation, international paperwork, and coordination. You focus on families.",
      highlight: "24/7 Live Support",
    },
    {
      icon: GlobeIcon,
      title: "Coverage",
      subtitle: "Unmatched Network",
      description:
        "Relationships with every major carrier mean 5-6 routing options per shipment. Domestic and international expertise with specialized rates and reliable service.",
      highlight: "5-6 Route Options",
    },
  ];

  return (
    <section id="why-csi" className="py-20 lg:py-32 bg-slate-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Section Header */}
        <div className="text-center max-w-3xl mx-auto mb-16">
          <div className="inline-flex items-center gap-2 bg-[#fef3c7] text-[#92400e] rounded-full px-4 py-2 text-sm font-medium mb-4">
            <ShieldIcon className="w-4 h-4" />
            The CSI Difference
          </div>
          <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold text-slate-900 mb-6">
            Why Funeral Directors{" "}
            <span className="text-[#1a4a82]">Choose Us</span>
          </h2>
          <p className="text-lg text-slate-600">
            We win on three dimensions that matter most: Cost, Convenience, and
            Coverage.
          </p>
        </div>

        {/* Advantages */}
        <div className="grid lg:grid-cols-3 gap-8">
          {advantages.map((item, index) => (
            <div
              key={index}
              className="relative bg-white rounded-3xl p-8 shadow-lg shadow-slate-200/50 border border-slate-100 overflow-hidden group"
            >
              {/* Top accent */}
              <div className="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-[#1a4a82] to-[#0ea5e9]" />

              {/* Icon */}
              <div className="w-16 h-16 bg-gradient-to-br from-[#dbeafe] to-[#e0f2fe] rounded-2xl flex items-center justify-center mb-6">
                <item.icon className="w-8 h-8 text-[#1a4a82]" />
              </div>

              <div className="mb-2">
                <span className="text-[#0ea5e9] font-semibold text-sm uppercase tracking-wider">
                  {item.title}
                </span>
              </div>
              <h3 className="text-2xl font-bold text-slate-900 mb-3">
                {item.subtitle}
              </h3>
              <p className="text-slate-600 mb-6">{item.description}</p>

              {/* Highlight badge */}
              <div className="inline-flex items-center gap-2 bg-gradient-to-r from-[#1a4a82] to-[#0ea5e9] text-white rounded-full px-4 py-2 text-sm font-semibold">
                <CheckIcon className="w-4 h-4" />
                {item.highlight}
              </div>
            </div>
          ))}
        </div>

        {/* Comparison Box */}
        <div className="mt-16 bg-white rounded-3xl p-8 lg:p-12 shadow-lg shadow-slate-200/50 border border-slate-100">
          <div className="text-center mb-10">
            <h3 className="text-2xl lg:text-3xl font-bold text-slate-900 mb-3">
              CSI vs. The Competition
            </h3>
            <p className="text-slate-600">
              See why more funeral homes are switching to CSI
            </p>
          </div>

          <div className="grid md:grid-cols-2 gap-8">
            {/* CSI Column */}
            <div className="bg-gradient-to-br from-[#dbeafe] to-[#e0f2fe] rounded-2xl p-6 border-2 border-[#1a4a82]">
              <div className="flex items-center gap-3 mb-6">
                <div className="w-10 h-10 rounded-full bg-[#1a4a82] flex items-center justify-center">
                  <PlaneIcon className="w-5 h-5 text-white" />
                </div>
                <span className="font-bold text-lg text-[#1a4a82]">
                  Cargo Sales International
                </span>
              </div>
              <ul className="space-y-3">
                {[
                  "Transparent pricing — published rates only",
                  "5-6 routing options per shipment",
                  "24/7 live agents, not call centers",
                  "Full international documentation",
                  "30-60 minute response times",
                  "Multi-carrier optimization",
                ].map((item, idx) => (
                  <li key={idx} className="flex items-start gap-2">
                    <CheckIcon className="w-5 h-5 text-green-600 flex-shrink-0 mt-0.5" />
                    <span className="text-slate-700">{item}</span>
                  </li>
                ))}
              </ul>
            </div>

            {/* Others Column */}
            <div className="bg-slate-100 rounded-2xl p-6">
              <div className="flex items-center gap-3 mb-6">
                <div className="w-10 h-10 rounded-full bg-slate-400 flex items-center justify-center">
                  <span className="text-white font-bold">?</span>
                </div>
                <span className="font-bold text-lg text-slate-600">
                  Traditional Providers
                </span>
              </div>
              <ul className="space-y-3">
                {[
                  "Hidden booking fees",
                  "1-2 routing options only",
                  "Call center ticket systems",
                  "Limited international support",
                  "Variable response times",
                  "Single carrier relationships",
                ].map((item, idx) => (
                  <li key={idx} className="flex items-start gap-2">
                    <CloseIcon className="w-5 h-5 text-red-500 flex-shrink-0 mt-0.5" />
                    <span className="text-slate-600">{item}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

// How It Works Section
function HowItWorksSection() {
  const steps = [
    {
      number: "01",
      title: "Submit Your Request",
      description:
        "Call or email us with shipment details. We gather decedent information, origin/destination, and timeline requirements.",
      icon: PhoneIcon,
    },
    {
      number: "02",
      title: "Receive Routing Options",
      description:
        "Within 30-60 minutes, get 5-6 optimized routing options with pricing, timing, and carrier reliability information.",
      icon: RouteIcon,
    },
    {
      number: "03",
      title: "We Handle Everything",
      description:
        "Once confirmed, we manage airline booking, cargo coordination, documentation, and all international paperwork.",
      icon: DocumentIcon,
    },
    {
      number: "04",
      title: "Real-Time Updates",
      description:
        "Track your shipment at every stage. We proactively communicate status and handle any exceptions that arise.",
      icon: ClockIcon,
    },
    {
      number: "05",
      title: "Safe Arrival",
      description:
        "We confirm destination release and coordinate with the receiving party for final delivery. Complete chain of custody.",
      icon: ShieldIcon,
    },
  ];

  return (
    <section id="how-it-works" className="py-20 lg:py-32 bg-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Section Header */}
        <div className="text-center max-w-3xl mx-auto mb-16">
          <div className="inline-flex items-center gap-2 bg-[#e0f2fe] text-[#0369a1] rounded-full px-4 py-2 text-sm font-medium mb-4">
            <RouteIcon className="w-4 h-4" />
            Simple Process
          </div>
          <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold text-slate-900 mb-6">
            How It <span className="text-[#1a4a82]">Works</span>
          </h2>
          <p className="text-lg text-slate-600">
            From your first call to safe arrival, we handle every detail with
            precision and care.
          </p>
        </div>

        {/* Steps */}
        <div className="relative">
          {/* Connection Line */}
          <div className="absolute top-0 bottom-0 left-1/2 w-0.5 bg-gradient-to-b from-[#1a4a82] via-[#0ea5e9] to-[#38bdf8] hidden lg:block" />

          <div className="space-y-12 lg:space-y-0">
            {steps.map((step, index) => (
              <div
                key={index}
                className={`relative lg:grid lg:grid-cols-2 lg:gap-12 ${
                  index !== steps.length - 1 ? "lg:pb-16" : ""
                }`}
              >
                {/* Content */}
                <div
                  className={`${index % 2 === 0 ? "lg:pr-16" : "lg:order-2 lg:pl-16"}`}
                >
                  <div
                    className={`bg-white border border-slate-200 rounded-2xl p-6 lg:p-8 shadow-sm hover:shadow-lg transition-shadow duration-300 ${
                      index % 2 === 0 ? "lg:text-right" : ""
                    }`}
                  >
                    <div
                      className={`flex items-center gap-4 mb-4 ${
                        index % 2 === 0 ? "lg:flex-row-reverse" : ""
                      }`}
                    >
                      <div className="w-12 h-12 bg-gradient-to-br from-[#1a4a82] to-[#0ea5e9] rounded-xl flex items-center justify-center">
                        <step.icon className="w-6 h-6 text-white" />
                      </div>
                      <span className="text-3xl font-bold text-[#0ea5e9]">
                        {step.number}
                      </span>
                    </div>
                    <h3 className="text-xl font-bold text-slate-900 mb-2">
                      {step.title}
                    </h3>
                    <p className="text-slate-600">{step.description}</p>
                  </div>
                </div>

                {/* Center Circle (desktop only) */}
                <div
                  className={`hidden lg:flex absolute left-1/2 top-8 -translate-x-1/2 w-4 h-4 bg-white border-4 border-[#1a4a82] rounded-full ${
                    index % 2 === 0 ? "" : ""
                  }`}
                />

                {/* Empty space for alternating layout */}
                <div className={index % 2 === 0 ? "lg:order-2" : ""} />
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}

// Testimonials Section
function TestimonialsSection() {
  const testimonials = [
    {
      quote:
        "CSI has transformed how we handle air shipments. The transparency and routing options are unmatched. We finally know exactly what we're paying for.",
      author: "Michael R.",
      role: "Funeral Director",
      location: "Chicago, IL",
    },
    {
      quote:
        "The 24/7 availability has been a game-changer. Knowing I can reach a real person at any hour gives us confidence to serve families better.",
      author: "Sarah T.",
      role: "Operations Manager",
      location: "Houston, TX",
    },
    {
      quote:
        "International repatriations used to be our biggest headache. CSI handles all the consulate work flawlessly. They've become essential to our operations.",
      author: "David K.",
      role: "Owner",
      location: "Los Angeles, CA",
    },
  ];

  return (
    <section className="py-20 lg:py-32 bg-slate-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        {/* Section Header */}
        <div className="text-center max-w-3xl mx-auto mb-16">
          <div className="inline-flex items-center gap-2 bg-[#fef3c7] text-[#92400e] rounded-full px-4 py-2 text-sm font-medium mb-4">
            <UsersIcon className="w-4 h-4" />
            Trusted by Professionals
          </div>
          <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold text-slate-900 mb-6">
            What Funeral Directors{" "}
            <span className="text-[#1a4a82]">Are Saying</span>
          </h2>
        </div>

        {/* Testimonials Grid */}
        <div className="grid md:grid-cols-3 gap-8">
          {testimonials.map((item, index) => (
            <div
              key={index}
              className="bg-white rounded-2xl p-8 shadow-lg shadow-slate-200/50 border border-slate-100 relative"
            >
              {/* Quote mark */}
              <div className="absolute top-6 right-6 text-6xl text-[#dbeafe] font-serif">
                &ldquo;
              </div>

              <p className="text-slate-700 mb-6 relative z-10 italic">
                &ldquo;{item.quote}&rdquo;
              </p>

              <div className="flex items-center gap-4">
                <div className="w-12 h-12 bg-gradient-to-br from-[#1a4a82] to-[#0ea5e9] rounded-full flex items-center justify-center text-white font-bold">
                  {item.author
                    .split(" ")
                    .map((n) => n[0])
                    .join("")}
                </div>
                <div>
                  <div className="font-semibold text-slate-900">
                    {item.author}
                  </div>
                  <div className="text-sm text-slate-500">
                    {item.role}, {item.location}
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

// CTA Section
function CTASection() {
  return (
    <section id="contact" className="py-20 lg:py-32 gradient-cta relative overflow-hidden">
      {/* Background elements */}
      <div className="absolute inset-0 overflow-hidden">
        <div className="absolute top-10 left-10 w-64 h-64 bg-white/5 rounded-full blur-3xl" />
        <div className="absolute bottom-10 right-10 w-96 h-96 bg-[#0ea5e9]/10 rounded-full blur-3xl" />
      </div>

      <div className="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid lg:grid-cols-2 gap-12 items-center">
          {/* Left Content */}
          <div className="text-center lg:text-left">
            <h2 className="text-3xl sm:text-4xl lg:text-5xl font-bold text-white mb-6">
              Ready to Experience the{" "}
              <span className="text-[#38bdf8]">CSI Difference?</span>
            </h2>
            <p className="text-lg text-white/80 mb-8">
              Join funeral homes nationwide who trust CSI for reliable,
              transparent air cargo logistics. Get started with a free quote
              today.
            </p>

            {/* Contact Options */}
            <div className="flex flex-col sm:flex-row gap-4 mb-8">
              <a
                href="tel:+1-800-CSI-SHIP"
                className="flex items-center justify-center gap-3 bg-white text-[#1a4a82] px-6 py-4 rounded-xl font-semibold hover:shadow-lg transition-shadow"
              >
                <PhoneIcon className="w-5 h-5" />
                <span>1-800-CSI-SHIP</span>
              </a>
              <a
                href="mailto:info@cargosalesintl.com"
                className="flex items-center justify-center gap-3 glass text-white px-6 py-4 rounded-xl font-semibold hover:bg-white/20 transition-colors"
              >
                <MailIcon className="w-5 h-5" />
                <span>info@cargosalesintl.com</span>
              </a>
            </div>

            {/* Available badge */}
            <div className="inline-flex items-center gap-2 bg-white/10 backdrop-blur-sm border border-white/20 rounded-full px-4 py-2">
              <span className="w-2 h-2 bg-green-400 rounded-full animate-pulse" />
              <span className="text-white/90 text-sm">
                Live agents available 24/7/365
              </span>
            </div>
          </div>

          {/* Right Content - Contact Form */}
          <div className="bg-white rounded-3xl p-8 shadow-2xl">
            <h3 className="text-2xl font-bold text-slate-900 mb-6">
              Request a Quote
            </h3>
            <form className="space-y-4">
              <div className="grid sm:grid-cols-2 gap-4">
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">
                    First Name
                  </label>
                  <input
                    type="text"
                    className="w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-[#1a4a82] focus:ring-2 focus:ring-[#dbeafe] outline-none transition-all"
                    placeholder="John"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-1">
                    Last Name
                  </label>
                  <input
                    type="text"
                    className="w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-[#1a4a82] focus:ring-2 focus:ring-[#dbeafe] outline-none transition-all"
                    placeholder="Doe"
                  />
                </div>
              </div>
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1">
                  Funeral Home Name
                </label>
                <input
                  type="text"
                  className="w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-[#1a4a82] focus:ring-2 focus:ring-[#dbeafe] outline-none transition-all"
                  placeholder="Memorial Funeral Home"
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1">
                  Email
                </label>
                <input
                  type="email"
                  className="w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-[#1a4a82] focus:ring-2 focus:ring-[#dbeafe] outline-none transition-all"
                  placeholder="john@funeralhome.com"
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1">
                  Phone
                </label>
                <input
                  type="tel"
                  className="w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-[#1a4a82] focus:ring-2 focus:ring-[#dbeafe] outline-none transition-all"
                  placeholder="(555) 123-4567"
                />
              </div>
              <div>
                <label className="block text-sm font-medium text-slate-700 mb-1">
                  How can we help?
                </label>
                <textarea
                  rows={3}
                  className="w-full px-4 py-3 rounded-xl border border-slate-200 focus:border-[#1a4a82] focus:ring-2 focus:ring-[#dbeafe] outline-none transition-all resize-none"
                  placeholder="Tell us about your shipment needs..."
                />
              </div>
              <button
                type="submit"
                className="w-full bg-gradient-to-r from-[#1a4a82] to-[#0ea5e9] text-white py-4 rounded-xl font-semibold text-lg hover:shadow-lg hover:shadow-[#1a4a82]/25 transition-all duration-300 flex items-center justify-center gap-2"
              >
                Submit Request
                <ArrowRightIcon className="w-5 h-5" />
              </button>
            </form>
          </div>
        </div>
      </div>
    </section>
  );
}

// Footer
function Footer() {
  return (
    <footer className="bg-[#0c1929] text-white py-16">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid md:grid-cols-4 gap-12 mb-12">
          {/* Brand */}
          <div className="md:col-span-2">
            <div className="flex items-center gap-2 mb-4">
              <div className="w-10 h-10 rounded-full bg-gradient-to-br from-[#1a4a82] to-[#0ea5e9] flex items-center justify-center">
                <PlaneIcon className="w-5 h-5 text-white" />
              </div>
              <div>
                <span className="font-bold text-lg">CSI</span>
                <span className="text-slate-400 text-sm ml-2">
                  Cargo Sales International
                </span>
              </div>
            </div>
            <p className="text-slate-400 mb-6 max-w-md">
              Your trusted partner for human remains air cargo logistics.
              Providing transparent, reliable service to funeral homes
              nationwide since day one.
            </p>
            <div className="flex gap-4">
              <a
                href="tel:+1-800-CSI-SHIP"
                className="flex items-center gap-2 text-slate-300 hover:text-white transition-colors"
              >
                <PhoneIcon className="w-4 h-4" />
                1-800-CSI-SHIP
              </a>
              <a
                href="mailto:info@cargosalesintl.com"
                className="flex items-center gap-2 text-slate-300 hover:text-white transition-colors"
              >
                <MailIcon className="w-4 h-4" />
                info@cargosalesintl.com
              </a>
            </div>
          </div>

          {/* Quick Links */}
          <div>
            <h4 className="font-semibold mb-4">Quick Links</h4>
            <ul className="space-y-2">
              <li>
                <a
                  href="#services"
                  className="text-slate-400 hover:text-white transition-colors"
                >
                  Services
                </a>
              </li>
              <li>
                <a
                  href="#why-csi"
                  className="text-slate-400 hover:text-white transition-colors"
                >
                  Why CSI
                </a>
              </li>
              <li>
                <a
                  href="#how-it-works"
                  className="text-slate-400 hover:text-white transition-colors"
                >
                  How It Works
                </a>
              </li>
              <li>
                <a
                  href="#contact"
                  className="text-slate-400 hover:text-white transition-colors"
                >
                  Contact
                </a>
              </li>
            </ul>
          </div>

          {/* Services */}
          <div>
            <h4 className="font-semibold mb-4">Services</h4>
            <ul className="space-y-2">
              <li className="text-slate-400">Domestic Shipping</li>
              <li className="text-slate-400">International Repatriation</li>
              <li className="text-slate-400">Documentation Handling</li>
              <li className="text-slate-400">Consulate Processing</li>
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
      <WhyCSISection />
      <HowItWorksSection />
      <TestimonialsSection />
      <CTASection />
      <Footer />
    </main>
  );
}
