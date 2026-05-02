"use client";

import { motion } from "framer-motion";
import Link from "next/link";
import { ArrowLeft, FileText, Construction } from "lucide-react";

export default function BITPage() {
  return (
    <div className="relative pt-28 pb-20 px-6">
      <div className="mx-auto max-w-2xl text-center">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
        >
          <div className="inline-flex items-center justify-center w-20 h-20 rounded-3xl bg-teal-50 text-teal-500 mb-8">
            <FileText className="w-10 h-10" />
          </div>
          <h1 className="text-3xl md:text-4xl font-extrabold text-slate-900 mb-4">
            BIT <span className="text-gradient">Question Papers</span>
          </h1>
          <p className="text-slate-500 mb-8 max-w-md mx-auto">
            Bachelor of Information Technology past exam papers and answer sheets. Coming soon.
          </p>

          <div className="inline-flex items-center gap-2 px-5 py-3 rounded-2xl bg-amber-50 border border-amber-100 text-amber-700 text-sm font-medium">
            <Construction className="w-4 h-4" />
            Content will be added after BA is complete
          </div>

          <div className="mt-10">
            <Link
              href="/"
              className="inline-flex items-center gap-2 text-sm text-slate-400 hover:text-sky-600 transition-colors"
            >
              <ArrowLeft className="w-4 h-4" />
              Back to Home
            </Link>
          </div>
        </motion.div>
      </div>
    </div>
  );
}
