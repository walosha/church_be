import React, { useState } from "react";
import { useForm } from "react-hook-form";
import { yupResolver } from "@hookform/resolvers/yup";
import AuthForm from "../../../components/authForm";
import { schema } from "./validation";
import { inputOptions } from "./contant";
import { useNavigate } from "react-router-dom";
import Helmet from "../../../components/helmet";

export default function SignUp() {
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const {
    handleSubmit,
    control,
    setError,
    formState: { errors, isSubmitting },
  } = useForm({
    defaultValues: {
      fullname: "",
      email: "",
      password: "",
    },
    resolver: yupResolver(schema),
  });

  return (
    <Helmet title="Welcome">
      <AuthForm
        title="Hi, Welcome"
        intro="Please sign-in to your account and start your experience"
        route="/login"
        btmText="Already have an account?"
        routeText="Login"
        btnText="REGISTER"
        inputOptions={inputOptions}
        handleSubmit={handleSubmit(() => {})}
        control={control}
        errors={errors}
        isLoading={isSubmitting || loading}
      />
    </Helmet>
  );
}
