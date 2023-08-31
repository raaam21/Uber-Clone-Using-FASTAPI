import React from 'react'
import './Login.css'

function Login() {
  return (
    
    <div className="login">
        <form className='login-container'>
            <h2 id='heading'> Sign In</h2>
            <label htmlFor='username'>Username</label>
            <input type='text' name='username' id='username'/>
            <label htmlFor="password">Password</label>            
            <input type='password' name='password' id='password'/>
        </form>

    </div>
  )
}

export default Login