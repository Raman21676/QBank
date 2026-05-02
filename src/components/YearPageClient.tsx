"use client";

import { motion } from "framer-motion";
import Link from "next/link";
import {
  ArrowLeft,
  Download,
  FileText,
  CheckCircle,
  Calendar,
  Clock,
  Award,
  Lock,
} from "lucide-react";
import type { FacultyManifest, Semester, Subject, Paper } from "@/lib/data";

export function YearPageClient({
  faculty,
  semester,
  subject,
  paper,
}: {
  faculty: FacultyManifest;
  semester: Semester;
  subject: Subject;
  paper: Paper;
}) {
  const questionPdf = `/pdfs/${faculty.slug}/${semester.slug}/${subject.slug}/questions/${subject.code}-${paper.year}.pdf`;
  const answerPdf = `/pdfs/${faculty.slug}/${semester.slug}/${subject.slug}/answers/${subject.code}-${paper.year}-answers.pdf`;

  return (
    <>
      {/* Breadcrumb */}
      <motion.div
        initial={{ opacity: 0, y: 10 }}
        animate={{ opacity: 1, y: 0 }}
        className="mb-8"
      >
        <Link
          href={`/${faculty.slug}/${semester.slug}/${subject.slug}/`}
          className="inline-flex items-center gap-1 text-sm text-slate-400 hover:text-sky-600 transition-colors"
        >
          <ArrowLeft className="w-4 h-4" />
          Back to {subject.name}
        </Link>
      </motion.div>

      {/* Paper Card */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="mb-8"
      >
        <div className="relative overflow-hidden rounded-3xl bg-white border border-slate-100 shadow-lg">
          {/* Top gradient bar */}
          <div className="h-2 bg-gradient-to-r from-sky-400 to-leaf-400" />

          <div className="p-8">
            {/* Meta */}
            <div className="flex flex-wrap items-center gap-3 mb-6">
              <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-sky-50 text-sky-600 text-xs font-semibold">
                <Calendar className="w-3.5 h-3.5" />
                {paper.year}
              </span>
              <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-slate-50 text-slate-500 text-xs font-medium">
                <Clock className="w-3.5 h-3.5" />
                {paper.duration || "3 Hours"}
              </span>
              <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-slate-50 text-slate-500 text-xs font-medium">
                <Award className="w-3.5 h-3.5" />
                FM: {paper.fm || 60} | PM: {paper.pm || 24}
              </span>
            </div>

            {/* Title */}
            <h1 className="text-2xl md:text-3xl font-extrabold text-slate-900 mb-2">
              {subject.name}
            </h1>
            <p className="text-sm font-mono text-slate-400 mb-6">
              {subject.code} &middot; {semester.name} &middot; Tribhuvan University &middot; {faculty.shortName}
            </p>

            {/* Description */}
            <p className="text-slate-500 text-sm leading-relaxed mb-8">
              This question paper contains Group A (MCQs), Group B (Short
              Answer), and Group C (Long Answer) questions. Download the
              question paper PDF to practice, or get the comprehensive answer
              sheet with detailed solutions, code examples, and diagrams.
            </p>

            {/* Download Buttons */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              {paper.hasQuestions ? (
                <a
                  href={questionPdf}
                  download
                  className="group flex items-center gap-4 p-5 rounded-2xl bg-sky-50 border border-sky-100 hover:bg-sky-100 hover:border-sky-200 transition-all duration-200"
                >
                  <div className="flex items-center justify-center w-12 h-12 rounded-xl bg-white text-sky-500 shadow-sm">
                    <FileText className="w-6 h-6" />
                  </div>
                  <div className="flex-1">
                    <h3 className="text-sm font-semibold text-slate-800">
                      Question Paper
                    </h3>
                    <p className="text-xs text-slate-400 mt-0.5">
                      PDF &middot; Past exam questions
                    </p>
                  </div>
                  <Download className="w-5 h-5 text-sky-400 group-hover:text-sky-600 group-hover:translate-y-0.5 transition-all" />
                </a>
              ) : (
                <div className="flex items-center gap-4 p-5 rounded-2xl bg-slate-50 border border-slate-100 opacity-70">
                  <div className="flex items-center justify-center w-12 h-12 rounded-xl bg-white text-slate-400 shadow-sm">
                    <Lock className="w-6 h-6" />
                  </div>
                  <div className="flex-1">
                    <h3 className="text-sm font-semibold text-slate-600">
                      Question Paper
                    </h3>
                    <p className="text-xs text-slate-400 mt-0.5">
                      Coming soon
                    </p>
                  </div>
                </div>
              )}

              {paper.hasAnswers ? (
                <a
                  href={answerPdf}
                  download
                  className="group flex items-center gap-4 p-5 rounded-2xl bg-leaf-50 border border-leaf-100 hover:bg-leaf-100 hover:border-leaf-200 transition-all duration-200"
                >
                  <div className="flex items-center justify-center w-12 h-12 rounded-xl bg-white text-leaf-500 shadow-sm">
                    <CheckCircle className="w-6 h-6" />
                  </div>
                  <div className="flex-1">
                    <h3 className="text-sm font-semibold text-slate-800">
                      Answer Sheet
                    </h3>
                    <p className="text-xs text-slate-400 mt-0.5">
                      PDF &middot; With solutions & diagrams
                    </p>
                  </div>
                  <Download className="w-5 h-5 text-leaf-400 group-hover:text-leaf-600 group-hover:translate-y-0.5 transition-all" />
                </a>
              ) : (
                <div className="flex items-center gap-4 p-5 rounded-2xl bg-slate-50 border border-slate-100 opacity-70">
                  <div className="flex items-center justify-center w-12 h-12 rounded-xl bg-white text-slate-400 shadow-sm">
                    <Lock className="w-6 h-6" />
                  </div>
                  <div className="flex-1">
                    <h3 className="text-sm font-semibold text-slate-600">
                      Answer Sheet
                    </h3>
                    <p className="text-xs text-slate-400 mt-0.5">
                      Coming soon
                    </p>
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>
      </motion.div>

      {/* Info Box */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.1 }}
        className="p-6 rounded-2xl bg-amber-50 border border-amber-100"
      >
        <h3 className="text-sm font-semibold text-amber-800 mb-2">
          About Answer Sheets
        </h3>
        <p className="text-sm text-amber-700/80 leading-relaxed">
          Each answer sheet includes the complete question rewritten for
          reference, followed by detailed step-by-step solutions. Programming
          questions include working code examples. Questions requiring diagrams
          (ER diagrams, flowcharts, circuit diagrams, etc.) include properly
          labeled illustrations.
        </p>
      </motion.div>
    </>
  );
}
