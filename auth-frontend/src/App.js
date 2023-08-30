import NavBar from './components/NavBar';
import axios from 'axios';



function App() {
  const  users = axios.get('http://127.0.0.1:8000/api/v3/users')
                          .then((res)=>console.log(res.data))
  
  const app_var = "App_variable" ;
  return (
    <div>
      <NavBar/> 
      <h1>this is {app_var} !!</h1>
    </div>
  );
}
export default App;
