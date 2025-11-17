"use client";

type BackendResponse = {
  ok: boolean;
  status: number;
  statusText: string;
  data: any;
};

import { useEffect, useState } from "react";

export default function Page() {
const [responseInfo, setResponseInfo] = useState<BackendResponse | null>(null);

useEffect(() => {
  fetch("http://localhost:8000")
    .then(async (res) => {
      const body = await res.json();

      setResponseInfo({
        ok: res.ok,
        status: res.status,
        statusText: res.statusText,
        data: body,
      });
    })
    .catch((err) => {
      setResponseInfo({
        ok: false,
        status: 0,
        statusText: err.message,
        data: null,
      });
    });
}, []);

  return (
    <div>
      <h1>Resposta do Backend</h1>
      <pre>{JSON.stringify(responseInfo, null, 2)}</pre>
    </div>
  );
}
