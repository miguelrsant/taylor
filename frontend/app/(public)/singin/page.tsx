"use client";

import { useState } from "react";

export default function Page() {
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setLoading(true);
    setMessage("");

    const form = e.currentTarget;
    const email = (form.elements.namedItem("email") as HTMLInputElement).value;
    const password = (form.elements.namedItem("password") as HTMLInputElement)
      .value;

    try {
      const res = await fetch(`/api/singin/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ email, password }),
      });

      if (!res.ok) {
        const data = await res.json();
        setMessage(
          data.msg || "❌ Algo deu errado. Tente novamente em instantes."
        );
        return;
      }

      setMessage("🎉 Seu login foi confirmado!");
      setTimeout(() => {
        window.location.href = "/auth/me";
      }, 500);
      form.reset();
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="waitingline">
      <div className="card-waitingline">
        <h1 className="waiting-taylor text-gradient">TAYLOR</h1>

        <p>
          Faça seu cadastro para acessar sua conta e aproveitar todos os
          recursos da plataforma.
        </p>

        <div className="cadastro-taylor">
          <form className="form-cadastro" onSubmit={handleSubmit}>
            <input
              type="email"
              name="email"
              placeholder="joaozinho@email.com"
              required
            />
            <input
              type="password"
              name="password"
              placeholder="********"
              required
            />

            <button
              type="submit"
              disabled={loading}
              style={{ cursor: "pointer" }}
            >
              {loading ? "Logando..." : "Logar"}
            </button>
          </form>
          <a
            href="/recover"
            style={{ color: "white" }}
            rel="noopener noreferrer"
          >
            Forgot your password?
          </a>
          {message && (
            <p
              className="status-message"
              style={{
                marginTop: "12px",
                fontWeight: 600,
                textAlign: "center",
              }}
            >
              {message}
            </p>
          )}

          <p className="p-footer">
            Designed & Developed by{" "}
            <strong>
              <a
                className="text-gradient"
                href="https://www.linkedin.com/in/miguelrsant/"
              >
                Miguel Angelo
              </a>
            </strong>
          </p>
        </div>
      </div>
    </div>
  );
}
