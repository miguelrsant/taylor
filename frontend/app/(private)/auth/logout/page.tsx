"use client";

export default function LogoutPage() {
  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    await fetch("/api/logout", {
      method: "POST",
    });

    window.location.href = "/singin";
  };

  return (
    <div className="waitingline">
      <form onSubmit={handleSubmit}>
        <button type="submit" style={{ cursor: "pointer" }}>
          Logout
        </button>
      </form>
    </div>
  );
}
