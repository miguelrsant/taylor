"use client";

import Home from "@/components/home-page/home";
import Pilares from "@/components/home-page/pilares";
import Escolher from "@/components/home-page/escolher";
import Impulsionam from "@/components/home-page/impulsionam";
import Negocio from "@/components/home-page/negocio";
import Logind from "@/components/home-page/loding";
import { useLayoutEffect } from "react";

export default function HomePage() {
  useLayoutEffect(() => {
    requestAnimationFrame(() => {
      window.scrollTo(0, 0);
      setTimeout(() => window.scrollTo(0, 0), 50);
    });
  }, []);

  return (
    <div className="all-content">
      <Logind></Logind>
      <Home></Home>
      <Pilares></Pilares>
      <Escolher></Escolher>
      <Impulsionam></Impulsionam>
      <Negocio></Negocio>
    </div>
  );
}
