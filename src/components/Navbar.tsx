"use client";

import { useState } from "react";
import Link from "next/link";
import { motion, AnimatePresence } from "framer-motion";
import { BookOpen, Menu, X, GraduationCap, Search } from "lucide-react";
import { cn } from "@/lib/utils";
import { SearchModal } from "./SearchModal";

const navLinks = [
  { href: "/", label: "Home" },
  { href: "/bca/", label: "BCA" },
  { href: "/ba/", label: "BA" },
  { href: "/bit/", label: "BIT" },
];

export function Navbar() {
  const [mobileOpen, setMobileOpen] = useState(false);
  const [searchOpen, setSearchOpen] = useState(false);

  return (
    <>
      <motion.header
        initial={{ y: -100 }}
        animate={{ y: 0 }}
        transition={{ type: "spring", stiffness: 100, damping: 20 }}
        className="fixed top-0 left-0 right-0 z-50"
      >
        <nav className="glass mx-4 mt-4 rounded-2xl px-6 py-3 md:mx-8 md:mt-6 md:px-8">
          <div className="flex items-center justify-between">
            {/* Logo */}
            <Link href="/" className="flex items-center gap-2 group">
              <div className="relative flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-sky-400 to-leaf-400 shadow-lg shadow-sky-200/50 group-hover:shadow-sky-300/60 transition-shadow">
                <GraduationCap className="w-6 h-6 text-white" />
              </div>
              <div className="flex flex-col">
                <span className="text-lg font-bold text-slate-800 leading-tight">
                  TU <span className="text-gradient">QBank</span>
                </span>
                <span className="text-[10px] text-slate-500 font-medium uppercase tracking-wider hidden sm:block">
                  Past Questions Archive
                </span>
              </div>
            </Link>

            {/* Desktop Links + Search */}
            <div className="hidden md:flex items-center gap-1">
              {navLinks.map((link) => (
                <Link
                  key={link.href}
                  href={link.href}
                  className={cn(
                    "px-4 py-2 rounded-xl text-sm font-medium transition-all duration-200",
                    "hover:bg-sky-50 hover:text-sky-600 text-slate-600"
                  )}
                >
                  {link.label}
                </Link>
              ))}
              <button
                onClick={() => setSearchOpen(true)}
                className="ml-2 flex items-center gap-2 px-3 py-2 rounded-xl bg-slate-50 hover:bg-sky-50 text-slate-500 hover:text-sky-600 transition-all duration-200"
              >
                <Search className="w-4 h-4" />
                <span className="text-xs font-medium hidden lg:inline">Search</span>
                <kbd className="hidden lg:inline-flex px-1.5 py-0.5 bg-white rounded text-[10px] text-slate-400 border border-slate-200">
                  ⌘K
                </kbd>
              </button>
            </div>

            {/* Mobile Search + Toggle */}
            <div className="flex items-center gap-2 md:hidden">
              <button
                onClick={() => setSearchOpen(true)}
                className="p-2 rounded-xl hover:bg-sky-50 text-slate-600 transition-colors"
              >
                <Search className="w-5 h-5" />
              </button>
              <button
                onClick={() => setMobileOpen(!mobileOpen)}
                className="p-2 rounded-xl hover:bg-sky-50 text-slate-600 transition-colors"
              >
                {mobileOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
              </button>
            </div>
          </div>

          {/* Mobile Menu */}
          <AnimatePresence>
            {mobileOpen && (
              <motion.div
                initial={{ opacity: 0, height: 0 }}
                animate={{ opacity: 1, height: "auto" }}
                exit={{ opacity: 0, height: 0 }}
                className="md:hidden mt-3 pt-3 border-t border-slate-100"
              >
                <div className="flex flex-col gap-1">
                  {navLinks.map((link) => (
                    <Link
                      key={link.href}
                      href={link.href}
                      onClick={() => setMobileOpen(false)}
                      className="px-4 py-3 rounded-xl text-sm font-medium text-slate-600 hover:bg-sky-50 hover:text-sky-600 transition-colors"
                    >
                      {link.label}
                    </Link>
                  ))}
                </div>
              </motion.div>
            )}
          </AnimatePresence>
        </nav>
      </motion.header>

      <SearchModal isOpen={searchOpen} onClose={() => setSearchOpen(false)} />
    </>
  );
}
