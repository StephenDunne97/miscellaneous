import logo from '../img/red_triangle.png';
import "./Header.css";

function Header() {
    return (
        <header className="Header">
            <img src={logo} className='header-logo' alt='logo-red-triangle'></img>
            <p className='header-text'>SnookerloopAPI</p>
        </header>
    );
}

export default Header;