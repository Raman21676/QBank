import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { Navbar } from "@/components/Navbar";
import { Footer } from "@/components/Footer";

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-inter",
});

export const metadata: Metadata = {
  title: "TU QBank — Tribhuvan University Past Questions",
  description:
    "Access past exam question papers and comprehensive answer sheets for Tribhuvan University BCA, BA, and BIT programs. Download PDFs with detailed solutions.",
  keywords: [
    "TU questions",
    "Tribhuvan University",
    "BCA past questions",
    "BA old questions",
    "BIT question papers",
    "Nepal university exams",
  ],
  openGraph: {
    title: "TU QBank — Tribhuvan University Past Questions",
    description:
      "Download past exam papers and answer sheets for TU BCA, BA, and BIT programs.",
    type: "website",
    locale: "en_US",
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className={inter.variable}>
      <body className="min-h-screen bg-gradient-to-br from-sky-50 via-white to-leaf-50 font-sans">
        <Navbar />
        <main className="relative">{children}</main>
        <Footer />
      </body>
    </html>
  );
}
