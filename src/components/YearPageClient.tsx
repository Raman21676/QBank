"use client";

import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
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
  X,
  Eye,
} from "lucide-react";
import type { FacultyManifest, Semester, Subject, Paper } from "@/lib/data";
import { BASE_PATH } from "@/lib/config";

function PdfViewer({
  url,
  title,
  onClose,
}: {
  url: string;
  title: string;
  onClose: () => void;
}) {
  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      className="fixed inset-0 z-50 flex flex-col bg-slate-900/80 backdrop-blur-sm"
      onClick={onClose}
    >
      {/* Top bar */}
      <div
        className="flex items-center justify-between px-4 py-3 bg-white border-b border-slate-200 shadow-sm"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="flex items-center gap-3 min-w-0">
          <FileText className="w-5 h-5 text-sky-500 shrink-0" />
          <h2 className="text-sm font-semibold text-slate-800 truncate">
            {title}
          </h2>
        </div>
        <div className="flex items-center gap-2 shrink-0">
          <a
            href={url}
            download
            className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-sky-50 text-sky-600 text-xs font-medium hover:bg-sky-100 transition-colors"
            onClick={(e) => e.stopPropagation()}
          >
            <Download className="w-3.5 h-3.5" />
            Download
          </a>
          <button
            onClick={onClose}
            className="inline-flex items-center justify-center w-8 h-8 rounded-lg hover:bg-slate-100 transition-colors"
            aria-label="Close viewer"
          >
            <X className="w-4 h-4 text-slate-500" />
          </button>
        </div>
      </div>

      {/* PDF iframe */}
      <div className="flex-1 relative">
        <iframe
          src={url}
          title={title}
          className="absolute inset-0 w-full h-full bg-white"
          onClick={(e) => e.stopPropagation()}
        />
      </div>
    </motion.div>
  );
}

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
  const questionPdf = `${BASE_PATH}/pdfs/${faculty.slug}/${semester.slug}/${subject.slug}/questions/${subject.code}-${paper.year}.pdf`;
  const answerPdf = `${BASE_PATH}/pdfs/${faculty.slug}/${semester.slug}/${subject.slug}/answers/${subject.code}-${paper.year}-answers.pdf`;

  const [viewer, setViewer] = useState<
    { url: string; title: string } | null
  >(null);

  return (
    <>
      <AnimatePresence>
        {viewer && (
          <PdfViewer
            url={viewer.url}
            title={viewer.title}
            onClose={() => setViewer(null)}
          />
        )}
      </AnimatePresence>

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
              Answer), and Group C (Long Answer) questions. View the question
              paper PDF directly in your browser, or download it for offline
              study. The answer sheet includes detailed solutions, code
              examples, and diagrams.
            </p>

            {/* Action Buttons */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              {paper.hasQuestions ? (
                <button
                  onClick={() =>
                    setViewer({
                      url: questionPdf,
                      title: `${subject.name} ${paper.year} — Question Paper`,
                    })
                  }
                  className="group flex items-center gap-4 p-5 rounded-2xl bg-sky-50 border border-sky-100 hover:bg-sky-100 hover:border-sky-200 transition-all duration-200 text-left"
                >
                  <div className="flex items-center justify-center w-12 h-12 rounded-xl bg-white text-sky-500 shadow-sm">
                    <Eye className="w-6 h-6" />
                  </div>
                  <div className="flex-1">
                    <h3 className="text-sm font-semibold text-slate-800">
                      View Question Paper
                    </h3>
                    <p className="text-xs text-slate-400 mt-0.5">
                      Open in browser viewer
                    </p>
                  </div>
                  <Download
                    className="w-5 h-5 text-sky-400 group-hover:text-sky-600 group-hover:translate-y-0.5 transition-all"
                    onClick={(e) => {
                      e.stopPropagation();
                      const a = document.createElement("a");
                      a.href = questionPdf;
                      a.download = "";
                      a.click();
                    }}
                  />
                </button>
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
                <button
                  onClick={() =>
                    setViewer({
                      url: answerPdf,
                      title: `${subject.name} ${paper.year} — Answer Sheet`,
                    })
                  }
                  className="group flex items-center gap-4 p-5 rounded-2xl bg-leaf-50 border border-leaf-100 hover:bg-leaf-100 hover:border-leaf-200 transition-all duration-200 text-left"
                >
                  <div className="flex items-center justify-center w-12 h-12 rounded-xl bg-white text-leaf-500 shadow-sm">
                    <Eye className="w-6 h-6" />
                  </div>
                  <div className="flex-1">
                    <h3 className="text-sm font-semibold text-slate-800">
                      View Answer Sheet
                    </h3>
                    <p className="text-xs text-slate-400 mt-0.5">
                      Open in browser viewer
                    </p>
                  </div>
                  <Download
                    className="w-5 h-5 text-leaf-400 group-hover:text-leaf-600 group-hover:translate-y-0.5 transition-all"
                    onClick={(e) => {
                      e.stopPropagation();
                      const a = document.createElement("a");
                      a.href = answerPdf;
                      a.download = "";
                      a.click();
                    }}
                  />
                </button>
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
