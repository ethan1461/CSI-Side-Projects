"use client";

import { useState } from "react";
import Link from "next/link";
import { Navigation, Footer } from "@/components/shared";

// Configuration for OMS integration
// When Kyri's front-end is ready, update this URL to embed or redirect
const OMS_FRONTEND_URL = process.env.NEXT_PUBLIC_OMS_URL || null;
const OMS_EMBED_MODE = process.env.NEXT_PUBLIC_OMS_EMBED === "true"; // iframe embed vs redirect

export default function BookPage() {
  const [formData, setFormData] = useState({
    // Shipper Info
    shipperName: "",
    shipperCompany: "",
    shipperEmail: "",
    shipperPhone: "",
    // Decedent Info
    decedentName: "",
    // Shipment Details
    serviceType: "",
    originCity: "",
    originState: "",
    destinationCity: "",
    destinationCountry: "",
    preferredDate: "",
    urgency: "",
    // Additional
    specialInstructions: "",
  });

  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submitted, setSubmitted] = useState(false);

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement>
  ) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsSubmitting(true);

    // TODO: Connect to OMS API endpoint when ready
    // const response = await fetch('/api/bookings', {
    //   method: 'POST',
    //   headers: { 'Content-Type': 'application/json' },
    //   body: JSON.stringify(formData),
    // });

    // Simulate API call for now
    await new Promise((resolve) => setTimeout(resolve, 1500));
    setIsSubmitting(false);
    setSubmitted(true);
  };

  // If OMS URL is configured and embed mode is on, show iframe
  if (OMS_FRONTEND_URL && OMS_EMBED_MODE) {
    return (
      <main className="min-h-screen bg-white">
        <Navigation />
        <div className="pt-24 pb-8 bg-gradient-to-b from-[#E0F2F5] to-white">
          <div className="max-w-7xl mx-auto px-4 text-center">
            <h1 className="text-3xl sm:text-4xl font-bold text-[#0c2940] mb-2">
              Book Your Shipment
            </h1>
            <p className="text-slate-600">
              Complete your booking using our secure portal below.
            </p>
          </div>
        </div>
        <div className="max-w-7xl mx-auto px-4 py-8">
          <iframe
            src={OMS_FRONTEND_URL}
            className="w-full min-h-[800px] border-0 rounded-xl shadow-lg"
            title="Cargo Sales Booking Portal"
          />
        </div>
        <Footer />
      </main>
    );
  }

  // If OMS URL is configured but not embed mode, show redirect button
  if (OMS_FRONTEND_URL && !OMS_EMBED_MODE) {
    return (
      <main className="min-h-screen bg-white">
        <Navigation />
        <section className="pt-32 pb-16 bg-gradient-to-b from-[#E0F2F5] to-white">
          <div className="max-w-4xl mx-auto px-4 text-center">
            <div className="inline-flex items-center justify-center w-20 h-20 bg-[#2E7BBF] rounded-full mb-6">
              <svg className="w-10 h-10 text-white" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <rect x="3" y="4" width="18" height="18" rx="2" ry="2" />
                <line x1="16" y1="2" x2="16" y2="6" />
                <line x1="8" y1="2" x2="8" y2="6" />
                <line x1="3" y1="10" x2="21" y2="10" />
              </svg>
            </div>
            <h1 className="text-4xl sm:text-5xl font-bold text-[#0c2940] mb-6">
              Book Your <span className="text-[#2E7BBF]">Shipment</span>
            </h1>
            <p className="text-lg text-slate-600 mb-8 max-w-2xl mx-auto">
              Access our booking portal to schedule your shipment, track orders,
              and manage your account.
            </p>
            <a
              href={OMS_FRONTEND_URL}
              className="inline-flex items-center gap-2 bg-[#2E7BBF] text-white px-8 py-4 rounded-full font-bold text-lg hover:bg-[#1E5A8F] hover:shadow-xl transition-all"
            >
              Go to Booking Portal
              <svg className="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <line x1="5" y1="12" x2="19" y2="12" />
                <polyline points="12 5 19 12 12 19" />
              </svg>
            </a>
            <p className="mt-6 text-slate-500 text-sm">
              Secure portal powered by Cargo Sales International
            </p>
          </div>
        </section>

        {/* Benefits */}
        <section className="py-16">
          <div className="max-w-7xl mx-auto px-4">
            <div className="grid md:grid-cols-3 gap-8">
              {[
                {
                  icon: (
                    <svg className="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                      <circle cx="12" cy="12" r="10" />
                      <polyline points="12 6 12 12 16 14" />
                    </svg>
                  ),
                  title: "Real-Time Tracking",
                  description: "Track your shipment status 24/7 from pickup to delivery.",
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
                  title: "Digital Documents",
                  description: "Access and manage all paperwork in one secure place.",
                },
                {
                  icon: (
                    <svg className="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                      <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
                    </svg>
                  ),
                  title: "Secure & Private",
                  description: "Your data is protected with enterprise-grade security.",
                },
              ].map((item, i) => (
                <div key={i} className="text-center">
                  <div className="w-16 h-16 bg-[#E0F2F5] rounded-full flex items-center justify-center mx-auto mb-4 text-[#2E7BBF]">
                    {item.icon}
                  </div>
                  <h3 className="font-bold text-[#0c2940] text-lg mb-2">{item.title}</h3>
                  <p className="text-slate-600">{item.description}</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        <Footer />
      </main>
    );
  }

  // Default: Show booking request form (before OMS is connected)
  if (submitted) {
    return (
      <main className="min-h-screen bg-white">
        <Navigation />
        <section className="pt-32 pb-16 min-h-[70vh] flex items-center">
          <div className="max-w-2xl mx-auto px-4 text-center">
            <div className="w-20 h-20 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-6">
              <svg className="w-10 h-10 text-green-600" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <polyline points="20 6 9 17 4 12" />
              </svg>
            </div>
            <h1 className="text-3xl sm:text-4xl font-bold text-[#0c2940] mb-4">
              Booking Request Received!
            </h1>
            <p className="text-slate-600 mb-8">
              Thank you for your request. Our team will review your shipment details
              and contact you within 1-2 hours with a quote and next steps.
            </p>
            <div className="bg-slate-50 rounded-xl p-6 mb-8">
              <p className="text-sm text-slate-500 mb-2">Need immediate assistance?</p>
              <a
                href="tel:+18662872583"
                className="text-[#2E7BBF] font-bold text-lg hover:underline"
              >
                Call +1 (866) 287-2583
              </a>
            </div>
            <Link
              href="/"
              className="text-[#2E7BBF] hover:underline"
            >
              Return to Home
            </Link>
          </div>
        </section>
        <Footer />
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-white">
      <Navigation />

      {/* Hero */}
      <section className="pt-32 pb-8 bg-gradient-to-b from-[#E0F2F5] to-white">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <h1 className="text-4xl sm:text-5xl font-bold text-[#0c2940] mb-4">
            Book a <span className="text-[#2E7BBF]">Shipment</span>
          </h1>
          <p className="text-lg text-slate-600 max-w-2xl mx-auto">
            Fill out the form below and our team will get back to you with a quote
            within 1-2 hours. Available 24/7.
          </p>
        </div>
      </section>

      {/* Booking Form */}
      <section className="py-8 pb-16">
        <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
          <form onSubmit={handleSubmit} className="space-y-8">
            {/* Contact Information */}
            <div className="bg-white rounded-2xl shadow-sm border border-slate-100 p-6 sm:p-8">
              <h2 className="text-xl font-bold text-[#0c2940] mb-6 flex items-center gap-2">
                <span className="w-8 h-8 bg-[#2E7BBF] text-white rounded-full flex items-center justify-center text-sm">1</span>
                Your Information
              </h2>
              <div className="grid sm:grid-cols-2 gap-6">
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-2">
                    Full Name *
                  </label>
                  <input
                    type="text"
                    name="shipperName"
                    required
                    value={formData.shipperName}
                    onChange={handleChange}
                    className="w-full px-4 py-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-[#2E7BBF] focus:border-transparent outline-none transition-all"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-2">
                    Funeral Home / Company *
                  </label>
                  <input
                    type="text"
                    name="shipperCompany"
                    required
                    value={formData.shipperCompany}
                    onChange={handleChange}
                    className="w-full px-4 py-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-[#2E7BBF] focus:border-transparent outline-none transition-all"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-2">
                    Email *
                  </label>
                  <input
                    type="email"
                    name="shipperEmail"
                    required
                    value={formData.shipperEmail}
                    onChange={handleChange}
                    className="w-full px-4 py-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-[#2E7BBF] focus:border-transparent outline-none transition-all"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-2">
                    Phone *
                  </label>
                  <input
                    type="tel"
                    name="shipperPhone"
                    required
                    value={formData.shipperPhone}
                    onChange={handleChange}
                    className="w-full px-4 py-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-[#2E7BBF] focus:border-transparent outline-none transition-all"
                  />
                </div>
              </div>
            </div>

            {/* Shipment Details */}
            <div className="bg-white rounded-2xl shadow-sm border border-slate-100 p-6 sm:p-8">
              <h2 className="text-xl font-bold text-[#0c2940] mb-6 flex items-center gap-2">
                <span className="w-8 h-8 bg-[#2E7BBF] text-white rounded-full flex items-center justify-center text-sm">2</span>
                Shipment Details
              </h2>
              <div className="grid sm:grid-cols-2 gap-6">
                <div className="sm:col-span-2">
                  <label className="block text-sm font-medium text-slate-700 mb-2">
                    Service Type *
                  </label>
                  <select
                    name="serviceType"
                    required
                    value={formData.serviceType}
                    onChange={handleChange}
                    className="w-full px-4 py-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-[#2E7BBF] focus:border-transparent outline-none transition-all bg-white"
                  >
                    <option value="">Select service type</option>
                    <option value="domestic">Domestic Shipping (within USA)</option>
                    <option value="international">International Repatriation</option>
                    <option value="cremated">Cremated Remains</option>
                    <option value="receiving">Receiving Services</option>
                  </select>
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-2">
                    Origin City *
                  </label>
                  <input
                    type="text"
                    name="originCity"
                    required
                    value={formData.originCity}
                    onChange={handleChange}
                    placeholder="e.g., Miami"
                    className="w-full px-4 py-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-[#2E7BBF] focus:border-transparent outline-none transition-all"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-2">
                    Origin State *
                  </label>
                  <input
                    type="text"
                    name="originState"
                    required
                    value={formData.originState}
                    onChange={handleChange}
                    placeholder="e.g., Florida"
                    className="w-full px-4 py-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-[#2E7BBF] focus:border-transparent outline-none transition-all"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-2">
                    Destination City *
                  </label>
                  <input
                    type="text"
                    name="destinationCity"
                    required
                    value={formData.destinationCity}
                    onChange={handleChange}
                    placeholder="e.g., Santo Domingo"
                    className="w-full px-4 py-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-[#2E7BBF] focus:border-transparent outline-none transition-all"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-2">
                    Destination Country *
                  </label>
                  <input
                    type="text"
                    name="destinationCountry"
                    required
                    value={formData.destinationCountry}
                    onChange={handleChange}
                    placeholder="e.g., Dominican Republic"
                    className="w-full px-4 py-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-[#2E7BBF] focus:border-transparent outline-none transition-all"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-2">
                    Preferred Ship Date
                  </label>
                  <input
                    type="date"
                    name="preferredDate"
                    value={formData.preferredDate}
                    onChange={handleChange}
                    className="w-full px-4 py-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-[#2E7BBF] focus:border-transparent outline-none transition-all"
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-2">
                    Urgency
                  </label>
                  <select
                    name="urgency"
                    value={formData.urgency}
                    onChange={handleChange}
                    className="w-full px-4 py-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-[#2E7BBF] focus:border-transparent outline-none transition-all bg-white"
                  >
                    <option value="">Select urgency</option>
                    <option value="standard">Standard (3-5 days)</option>
                    <option value="priority">Priority (1-2 days)</option>
                    <option value="urgent">Urgent (Same day / Next day)</option>
                  </select>
                </div>
                <div className="sm:col-span-2">
                  <label className="block text-sm font-medium text-slate-700 mb-2">
                    Special Instructions
                  </label>
                  <textarea
                    name="specialInstructions"
                    rows={3}
                    value={formData.specialInstructions}
                    onChange={handleChange}
                    placeholder="Any additional information or requirements..."
                    className="w-full px-4 py-3 border border-slate-200 rounded-xl focus:ring-2 focus:ring-[#2E7BBF] focus:border-transparent outline-none transition-all resize-none"
                  />
                </div>
              </div>
            </div>

            {/* Submit */}
            <div className="flex flex-col sm:flex-row gap-4 items-center justify-between">
              <p className="text-slate-500 text-sm order-2 sm:order-1">
                Need help? Call{" "}
                <a href="tel:+18662872583" className="text-[#2E7BBF] font-medium">
                  +1 (866) 287-2583
                </a>
              </p>
              <button
                type="submit"
                disabled={isSubmitting}
                className="w-full sm:w-auto order-1 sm:order-2 bg-[#2E7BBF] text-white px-8 py-4 rounded-full font-bold text-lg hover:bg-[#1E5A8F] hover:shadow-xl transition-all disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
              >
                {isSubmitting ? (
                  <>
                    <svg className="animate-spin w-5 h-5" viewBox="0 0 24 24">
                      <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" fill="none" />
                      <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z" />
                    </svg>
                    Submitting...
                  </>
                ) : (
                  <>
                    Submit Booking Request
                    <svg className="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                      <line x1="5" y1="12" x2="19" y2="12" />
                      <polyline points="12 5 19 12 12 19" />
                    </svg>
                  </>
                )}
              </button>
            </div>
          </form>

          {/* Trust indicators */}
          <div className="mt-12 pt-8 border-t border-slate-100">
            <div className="flex flex-wrap justify-center gap-8 text-slate-400 text-sm">
              <div className="flex items-center gap-2">
                <svg className="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
                </svg>
                IATA Certified
              </div>
              <div className="flex items-center gap-2">
                <svg className="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <circle cx="12" cy="12" r="10" />
                  <polyline points="12 6 12 12 16 14" />
                </svg>
                24/7 Support
              </div>
              <div className="flex items-center gap-2">
                <svg className="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <rect x="3" y="11" width="18" height="11" rx="2" ry="2" />
                  <path d="M7 11V7a5 5 0 0 1 10 0v4" />
                </svg>
                Secure & Private
              </div>
            </div>
          </div>
        </div>
      </section>

      <Footer />
    </main>
  );
}
