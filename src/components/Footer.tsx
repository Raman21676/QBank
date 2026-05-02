"use client";

import Link from "next/link";
import { GraduationCap, Heart, Github } from "lucide-react";

export function Footer() {
  return (
    <footer className="relative mt-24 border-t border-slate-200/60 bg-white/50 backdrop-blur-sm">
      <div className="mx-auto max-w-7xl px-6 py-12 md:px-8">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-10">
          {/* Brand */}
          <div className="space-y-4">
            <Link href="/" className="flex items-center gap-2">
              <div className="flex items-center justify-center w-9 h-9 rounded-lg bg-gradient-to-br from-sky-400 to-leaf-400">
                <GraduationCap className="w-5 h-5 text-white" />
              </div>
              <span className="text-lg font-bold text-slate-800">
                TU <span className="text-gradient">QBank</span>
              </span>
            </Link>
            <p className="text-sm text-slate-500 leading-relaxed max-w-xs">
              Your comprehensive archive of Tribhuvan University past exam
              questions and detailed answer sheets.
            </p>
          </div>

          {/* Quick Links */}
          <div>
            <h3 className="text-sm font-semibold text-slate-800 uppercase tracking-wider mb-4">
              Faculties
            </h3>
            <ul className="space-y-2.5">
              {[
                { label: "BCA", href: "/bca/" },
                { label: "BA", href: "/ba/" },
                { label: "BIT", href: "/bit/" },
              ].map((link) => (
                <li key={link.href}>
                  <Link
                    href={link.href}
                    className="text-sm text-slate-500 hover:text-sky-600 transition-colors"
                  >
                    {link.label}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          {/* Resources */}
          <div>
            <h3 className="text-sm font-semibold text-slate-800 uppercase tracking-wider mb-4">
              Resources
            </h3>
            <ul className="space-y-2.5">
              {[
                { label: "About", href: "#" },
                { label: "Contribute", href: "#" },
                { label: "Report Issue", href: "#" },
              ].map((link) => (
                <li key={link.label}>
                  <Link
                    href={link.href}
                    className="text-sm text-slate-500 hover:text-sky-600 transition-colors"
                  >
                    {link.label}
                  </Link>
                </li>
              ))}
            </ul>
          </div>
        </div>

        <div className="mt-10 pt-6 border-t border-slate-200/60 flex flex-col sm:flex-row items-center justify-between gap-4">
          <p className="text-xs text-slate-400">
            &copy; {new Date().getFullYear()} TU QBank. Not affiliated with
            Tribhuvan University.
          </p>
          <p className="text-xs text-slate-400 flex items-center gap-1">
            Built with <Heart className="w-3 h-3 text-red-400 fill-red-400" /> for TU students
          </p>
        </div>
      </div>
    </footer>
  );
}
