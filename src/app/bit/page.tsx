import { Metadata } from "next";
import { bitData } from "@/lib/data";
import { FacultyPageClient } from "@/components/FacultyPageClient";

export const metadata: Metadata = {
  title: "BIT — Bachelor of Information Technology | TU QBank",
  description:
    "Browse past exam papers and answer sheets for all 8 semesters of TU BIT program.",
};

export default function BITPage() {
  return <FacultyPageClient faculty={bitData} />;
}
