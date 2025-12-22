"use client";

import { useState } from "react";

export default function Recover() {
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [successMsg, setSuccessMsg] = useState<string | null>(null);
  const [errorMsg, setErrorMsg] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    const searchParams = new URL(window.location.href).searchParams;
    const token = searchParams.get("token");

    e.preventDefault();

    setLoading(true);
    setSuccessMsg(null);
    setErrorMsg(null);

    try {
      const res = await fetch("/api/reset-password", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ new_password: password, token: token }),
      });

      if (!res.ok) {
        let msg = `Request failed (${res.status})`;
        try {
          const data = await res.json();
          if (typeof data?.msg === "string") msg = data.msg;
        } catch {}
        throw new Error(msg);
      }

      setSuccessMsg("Senha Redefinida com sucesso. Você já pode fazer login.");
      setPassword("");
      setTimeout(() => {
        window.location.href = "/auth/me";
      }, 500);
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
          type="password"
          name="password"
          id="password"
          required
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="**********"
        />

        <button type="submit" disabled={loading}>
          {loading ? "Sending..." : "Send Reset Password"}
        </button>
      </form>

      {successMsg && <p>{successMsg}</p>}
      {errorMsg && <p>{errorMsg}</p>}
    </div>
  );
}
