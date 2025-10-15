import React, { useEffect, useState } from "react";
import axios from "axios";
import Menu from "./menu/menu";

const MontajIslemleri = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [expandedRow, setExpandedRow] = useState(null);
  const [arama, setArama] = useState("");

  const [currentPage, setCurrentPage] = useState(1);
  const rowsPerPage = 10;

  useEffect(() => {
    const fetchMontajVerisi = async () => {
      try {
        const technicianFullName = localStorage.getItem("technicianFullName");
        if (!technicianFullName) {
          console.error("Kullanıcı adı bulunamadı!");
          setLoading(false);
          return;
        }

        const res = await axios.get("http://localhost:5000/montajGetirFiltreli", {
          params: { technician: technicianFullName },
        });

        const filtered = res.data.filter(
          (row) => row.technicianFullName === technicianFullName
        );

        setData(filtered);
        setLoading(false);
      } catch (err) {
        console.error("Veri çekme hatası:", err);
        setLoading(false);
      }
    };

    fetchMontajVerisi();
  }, []);
  
  // Search filter (searches across all fields)
  const filteredData = data.filter((row) =>
    Object.values(row).some((val) =>
      String(val).toLowerCase().includes(arama.toLowerCase())
    )
  );

  // Pagination
  const indexOfLastRow = currentPage * rowsPerPage;
  const indexOfFirstRow = indexOfLastRow - rowsPerPage;
  const currentRows = filteredData.slice(indexOfFirstRow, indexOfLastRow);
  const totalPages = Math.ceil(data.length / rowsPerPage);

  // Style objects for UI component
  const rowStyle = {
    border: "1px solid #ccc",
    padding: "10px",
    cursor: "pointer",
    backgroundColor: "#f9f9f9",
    marginBottom: "5px",
    borderRadius: "6px",
  };

  const expandedStyle = {
    backgroundColor: "#fff",
    padding: "10px",
    borderTop: "1px solid #ddd",
    marginTop: "8px",
    fontSize: "14px",
    lineHeight: "1.4",
  };

  const paginationStyle = {
    marginTop: "10px",
    display: "flex",
    justifyContent: "center",
    gap: "10px",
    alignItems: "center",
  };

  const buttonStyle = {
    padding: "5px 10px",
    cursor: "pointer",
  };

  

  const aramaKutusuStyle = {
    padding: "6px",
    borderRadius: "6px",
    border: "1px solid #ccc",
    width: "250px",
  };

  return (
    <div style={{ display: "flex" }}>
      <Menu />
      <div style={{ padding: "20px", flex: 1 }}>
        <h2>Montaj İşlemleri</h2>
        <input
            type="text"
            placeholder="Ara..."
            value={arama}
            onChange={(e) => setArama(e.target.value)}
            style={aramaKutusuStyle}
        />
        {loading ? (
          <div>Yükleniyor...</div>
        ) : filteredData.length === 0 ? (
          <p>Hiç eşleşen veri bulunamadı.</p>
        ) : (
          <>
            {currentRows.map((row, index) => (
              <div
                key={index}
                style={rowStyle}
                onClick={() =>
                  setExpandedRow(expandedRow === index ? null : index)
                }
              >
                <strong>{row.activation_date}</strong> |{" "}
                <strong>{row.ttbServiceName}</strong> |{" "}
                <strong>{row.vehicleCompanyName}</strong> |{" "}
                <strong>{row.companyName}</strong> ({row.city}/{row.district}))
                {expandedRow === index && (
                  <div style={expandedStyle}>
                    <div><strong>Adres:</strong> {row.address}</div>
                    <div><strong>Tarih:</strong> {row.activation_date} - {row.activation_time} </div>
                    <div><strong>Firma:</strong> {row.ttbServiceName}</div>
                    <div><strong>Araç Plakası:</strong> {row.licensePlate}</div>
                    <div><strong>Teknisyen Adı:</strong> {row.technicianFullName}</div>
                    <div><strong>Sürücü E-mail:</strong> {row.driverEmail}</div>
                    <div><strong>Sürücü Tel:</strong> {row.driverPhoneNumber}</div>
                    <div><strong>Güncelleme Tarihi:</strong> {row.lastModified}</div>
                    <div><strong>Durum:</strong> {row.vehicleOrderInstallationStatus}</div>
                    {/* Additional columns can be added here */}
                  </div>
                )}
              </div>
            ))}

            {/* pagination */}
            <div style={paginationStyle}>
              <button
                style={buttonStyle}
                onClick={() => setCurrentPage((p) => Math.max(p - 1, 1))}
                disabled={currentPage === 1}
              >
                ◀
              </button>
              <span>Sayfa {currentPage} / {totalPages}</span>
              <button
                style={buttonStyle}
                onClick={() => setCurrentPage((p) => Math.min(p + 1, totalPages))}
                disabled={currentPage === totalPages}
              >
                ▶
              </button>
            </div>
          </>
        )}
      </div>
    </div>
  );
};

export default MontajIslemleri;
