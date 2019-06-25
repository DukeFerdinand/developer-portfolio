import React, { useState } from "react";
import getConfig from "next/config";

const { publicRuntimeConfig } = getConfig();
const { API_URL } = publicRuntimeConfig;

const testApi = async cb => {
  const res = await fetch(`/api/`).then(res => {
    console.log(res);
  });
};

function Home() {
  let [response, setResponse] = useState("Click for response");
  return (
    <div>
      Welcome to Next.js!
      <button onClick={() => testApi(setResponse)}>Test api</button>
    </div>
  );
}

export default Home;
