"use client";

import { useState } from "react";

export default function Recover() {
  const [email, setEmail] = useState("");
  const [loading, setLoading] = useState(false);
  const [successMsg, setSuccessMsg] = useState<string | null>(null);
  const [errorMsg, setErrorMsg] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    setLoading(true);
    setSuccessMsg(null);
    setErrorMsg(null);

    try {
      const res = await fetch("/api/recover", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email }),
      });

      if (!res.ok) {
        let msg = `Request failed (${res.status})`;
        try {
          const data = await res.json();
          if (typeof data?.msg === "string") msg = data.msg;
        } catch {}
        throw new Error(msg);
      }

      setSuccessMsg(
        "Email de recuperação enviado com sucesso. Verifique sua caixa de entrada."
      );
      setEmail("");
    } catch (err) {
      setErrorMsg(err instanceof Error ? err.message : "Unexpected error");
      console.error("Error submitting form:", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Password Recovery</h1>

      <form onSubmit={handleSubmit}>
        <input
          type="email"
          name="email"
          id="email"
          required
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="your@email.com"
        />

        <button type="submit" disabled={loading}>
          {loading ? "Sending..." : "Send Recovery Email"}
        </button>
      </form>

      {successMsg && <p>{successMsg}</p>}
      {errorMsg && <p>{errorMsg}</p>}
    </div>
  );
}
