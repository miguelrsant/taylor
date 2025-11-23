"use client"; 

import type { Metadata } from "next";

import '../public/styles/index.css' 
import React, { useEffect } from 'react';

const metadata: Metadata = {
  title: "Taylor: Business Super Intelligence Platform",
  description: "TAYLOR é uma plataforma avançada de automação operacional e análise inteligente, transformando dados em decisões estratégicas para empresas de todos os setores.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  
  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      const cursorOuter = document.querySelector('.cursor-outer') as HTMLElement | null;
      const cursorDot = document.querySelector('.cursor-dot') as HTMLElement | null;

      if (cursorDot && cursorOuter) {
        cursorDot.style.left = e.clientX + 'px';
        cursorDot.style.top = e.clientY + 'px';

        cursorOuter.style.left = e.clientX + 'px';
        cursorOuter.style.top = e.clientY + 'px';
      }
    };

    document.addEventListener('mousemove', handleMouseMove);

    return () => {
      document.removeEventListener('mousemove', handleMouseMove);
    };
  }, []);

  return (
    <html lang="pt-br"
    data-lt-installed="true">
      <head>
        <link rel="shortcut icon" href="./svg/taylor-logo-gradiente.svg"/>
      </head>
      <body>
        <div className="cursor-outer"></div>
        <div className="cursor-dot"></div>
        {children}
      </body>
    </html>
  );
}