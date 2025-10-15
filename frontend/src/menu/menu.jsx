import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import styled from 'styled-components';
import { FaHome, FaUser, FaBox, FaTruck, FaTools, FaClipboardList, FaCogs } from 'react-icons/fa';

const Sidebar = styled.div`
  width: 250px;
  height: 100vh;
  background-color: #1B1F3B;
  display: flex;
  flex-direction: column;
  padding: 20px;
  color: white;
  font-family: 'Segoe UI', sans-serif;
`;

const LogoContainer = styled.div`
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
`;

const Logo = styled.img`
  width: 200px;
  height: auto;
`;

const SearchBox = styled.input`
  padding: 10px;
  border-radius: 8px;
  border: none;
  outline: none;
  width: 100%;
  margin-bottom: 20px;
  font-size: 14px;
  background-color: #2C2F4A;
  color: white;

  &::placeholder {
    color: #aaa;
  }
`;

const MenuItems = styled.div`
  display: flex;
  flex-direction: column;
  gap: 10px;
`;

const MenuItem = styled(Link).attrs(props => ({
  $active: props.$active
}))`
  padding: 10px 15px;
  border-radius: 8px;
  font-size: 16px;
  color: ${({ $active }) => ($active ? '#fff' : '#ccc')};
  background-color: ${({ $active }) => ($active ? '#F97316' : 'transparent')};
  text-decoration: none;
  display: flex;
  align-items: center;
  transition: background-color 0.3s, color 0.3s;

  &:hover {
    background-color: #F97316;
    color: white;
  }

  svg {
    margin-right: 10px;
  }
`;

const Menu = () => {
  const location = useLocation();

  return (
    <Sidebar>
      <LogoContainer>
        <Logo src="/logo.png" alt="UTTS Logo" />
      </LogoContainer>
      <SearchBox type="text" placeholder="Arama Yap..." />
      <MenuItems>
        <MenuItem to="/dashboard" $active={location.pathname === "/dashboard"}><FaHome /> Anasayfa</MenuItem>
        <MenuItem to="#" $active={false}><FaUser /> Hesabım</MenuItem>
        <MenuItem to="#" $active={false}><FaBox /> Siparişler</MenuItem>
        <MenuItem to="#" $active={false}><FaClipboardList /> Stok Yönetimi</MenuItem>
        <MenuItem to="#" $active={false}><FaTruck /> Taşıtlarım</MenuItem>
        <MenuItem to="/dashboard/montaj_islemleri" $active={location.pathname.includes("montaj_islemleri")}><FaTools /> Montaj İşlemleri</MenuItem>
        <MenuItem to="#" $active={false}><FaClipboardList /> Kılavuzlar ve Yönergeler</MenuItem>
        <MenuItem to="#" $active={false}><FaCogs /> Teknisyen Yönetimi</MenuItem>
      </MenuItems>
    </Sidebar>
  );
};

export default Menu;
