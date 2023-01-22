import React, { useState } from "react";
import AuthForm from "../../../components/authForm";
import { useNavigate } from "react-router-dom";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import { schema } from "./validation";
import { inputOptions } from "./contant";
import Helmet from "../../../components/helmet";

export default function Login() {
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();
  const {
    handleSubmit,
    control,
    setError,
    formState: { errors, isSubmitting },
  } = useForm({
    defaultValues: {
      email: "",
      password: "",
    },
    resolver: yupResolver(schema),
  });

  return (
    <Helmet title="login">
      <AuthForm
        title="Hi, Welcome"
        intro="Please sign-up to start your experience"
        route="/"
        btmText="Don’t have an account?"
        routeText="Register"
        btnText="LOGIN"
        inputOptions={inputOptions}
        isLoading={isSubmitting || loading}
        handleSubmit={handleSubmit(() => {})}
        control={control}
        errors={errors}
      />
    </Helmet>
  );
}
