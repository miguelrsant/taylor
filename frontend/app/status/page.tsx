"use client";

type BackendResponse = {
  data: any;
};

import { useEffect, useState } from "react";

export default function Page() {
const [responseInfo, setResponseInfo] = useState<BackendResponse | null>(null);

useEffect(() => {
  fetch("http://localhost:8000/status/")
    .then(async (res) => {
      const body = await res.json();

      setResponseInfo({
        data: body,
      });
    })
}, []);

  return (
    <div>
      <h1>Resposta do Backend</h1>
      <pre>{JSON.stringify(responseInfo, null, 2)}</pre>
    </div>
  );
}
