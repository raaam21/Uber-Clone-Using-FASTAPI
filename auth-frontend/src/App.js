import NavBar from './components/NavBar';
import axios from 'axios';
import Login from './components/Login';
import './App.css'


function App() {
  const  users = axios.get('http://127.0.0.1:8000/api/v3/users')
                          .then((res)=>console.log(res.data))
  
  const app_var = "App_variable" ;
  return (
    <div className='app'>
      <NavBar/> 
      <Login/>
    </div>
  );
}
export default App;
