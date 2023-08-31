import React from 'react'
import './NavBar.css'

function NavBar() {
  return (
    <div className='navBar'> 
      <div className='NavBarLeft'>
        <ul>Uber</ul> 
        <ul>Company</ul>
        <ul>Safety</ul>
        <ul>Help</ul>
      
      </div>
     
      <div className='NavBarRight'>
          <button className='NavBar_login_Button'>Login</button>
          <button className='NavBar_Signup_Button' >Sign UP</button>
      </div>
    </div>

  )
}

export default NavBar