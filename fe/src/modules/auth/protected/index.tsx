import { Outlet, useNavigate } from "react-router-dom";

export default function ProtectedRoute(): JSX.Element {
  // const { currentUser } = useAuth();
  const navigate = useNavigate();
  // useEffect(() => {
  //   if (!currentUser) {
  //     navigate("/");
  //     return;
  //   }
  // });

  return <Outlet />;
}
