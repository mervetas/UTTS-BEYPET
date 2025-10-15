import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    console.log("🔐 Giriş butonuna basıldı");
    e.preventDefault();
  
    try {
      const res = await axios.post("http://localhost:5000/login", {
        email,
        password,
      });
  
      console.log("✅ Giriş başarılı:", res.data);
  
      if (res.status === 200 && res.data.technicianFullName) {
        localStorage.setItem("technicianFullName", res.data.technicianFullName);
        navigate("/dashboard");
      } else {
        console.log("⚠️ Beklenmeyen yanıt formatı:", res);
        setError("Girişte bir sorun oluştu.");
      }
    } catch (err) {
      console.log("❌ Giriş hatası:", err);
      setError("Hatalı e-posta veya şifre!");
    }
  };
  
  return (
    <div className="container d-flex justify-content-center align-items-center min-vh-100">
      <div className="card p-4" style={{ width: "350px", borderRadius: "15px" }}>
        <div className="text-center mb-3">
          <img src="/logo.png" alt="UTTS Logo" style={{ width: "300px", height: "auto", objectFit: "contain" }} />
        </div>
        
        <h2 className="text-center mb-4" style={{ fontSize: "24px", fontWeight: "bold" }}>Giriş Yap</h2>
        <p className="text-center mb-4" style={{ fontSize: "14px" }}>
          Ulusal Taşıt Tanıma Sistemi'ne kullanıcı adı ve şifrenizle giriş yapabilirsiniz.
        </p>

        <form onSubmit={handleLogin}>
          <div className="form-group mb-3">
            <label htmlFor="email" style={{ fontSize: "14px", fontWeight: "bold" }}>E-Posta :</label>
            <input
              type="email"
              id="email"
              placeholder="E-posta"
              className="form-control"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              style={{ fontSize: "14px" }}
            />
          </div>

          <div className="form-group mb-3">
            <label htmlFor="password" style={{ fontSize: "14px", fontWeight: "bold" }}>Şifre :</label>
            <input
              type="password"
              id="password"
              placeholder="Parola"
              className="form-control"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              style={{ fontSize: "14px" }}
            />
          </div>

          <button
            type="submit"
            className="btn btn-warning w-100"
            style={{
              borderRadius: "50px",
              fontWeight: "bold",
              fontSize: "16px",
              padding: "12px 0",
            }}
          >
            Giriş Yap
          </button>
        </form>

        {error && <div className="text-danger mt-3">{error}</div>} {/* Error message display */}
      </div>
    </div>
  );
}

export default Login;
