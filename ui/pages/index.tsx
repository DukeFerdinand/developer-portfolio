import React, { useState } from "react";

const testApi = async cb => {
  const res = await fetch(`/api/`).then(res => {
    console.log(res);
  });
};

const Home: React.SFC = () => {
  return <div>Home</div>;
};

export default Home;
