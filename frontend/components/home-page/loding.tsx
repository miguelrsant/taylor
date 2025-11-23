"use client";
import { useLayoutEffect } from "react";
import { gsap } from "gsap";

export default function Logind() {
  useLayoutEffect(() => {
    // força o scroll voltar ao topo antes e depois da hidratação
    requestAnimationFrame(() => {
      window.scrollTo(0, 0);
      setTimeout(() => window.scrollTo(0, 0), 50);
    });

    const scrollBarWidth =
      window.innerWidth - document.documentElement.clientWidth;

    if (scrollBarWidth > 0) {
      document.documentElement.style.marginRight = `${scrollBarWidth}px`;
    }

    document.documentElement.style.overflow = "hidden";

    gsap.fromTo(
      ".loging-page",
      { opacity: 1 },
      {
        opacity: 0,
        duration: 1.5,
        delay: 1.9,
        display: "none",
        onComplete: () => {
          document.documentElement.style.overflow = "auto";
          document.documentElement.style.marginRight = "0px";
        },
      }
    );

    return () => {
      document.documentElement.style.overflow = "auto";
      document.documentElement.style.marginRight = "0px";
    };
  }, []);

  return (
    <div className="loging-page">
      <svg
        className="loding-svg"
        xmlns="http://www.w3.org/2000/svg"
        width="512"
        height="512"
        viewBox="0 0 24 24"
        fill="#000000"
      >
        <g fill="none" stroke="#000000">
          <circle cx="19" cy="5" r="2.5" strokeWidth="0.5" />
          <path
            strokeLinecap="round"
            strokeWidth="1.5"
            d="M21.25 10v5.25a6 6 0 0 1-6 6h-6.5a6 6 0 0 1-6-6v-6.5a6 6 0 0 1 6-6H14"
          />
          <path
            strokeLinecap="round"
            strokeWidth="1.6"
            d="M8.276 16.036v-4.388m3.83 4.388V8.769m3.618 7.267v-5.51"
          />
        </g>
      </svg>
    </div>
  );
}
