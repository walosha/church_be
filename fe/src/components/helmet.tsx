import React from "react";
import { Helmet } from "react-helmet";

type HelmetProps = {
  children: React.ReactNode;
  title: string;
};

export default function ReactHelmet({ title, children }: HelmetProps) {
  return (
    <>
      <Helmet>
        <meta charSet="utf-8" />
        <title>{title}</title>
      </Helmet>
      {children}
    </>
  );
}
