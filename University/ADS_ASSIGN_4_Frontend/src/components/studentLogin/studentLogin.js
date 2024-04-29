import axios from "axios";
import React from "react";
import { useNavigate } from "react-router-dom";
import "./studentLogin.css";

function StudentLogin() {
    const navigate = useNavigate();
    return (
        <div style={{ textAlign: "center", fontFamily: "verdana" }}>
            <h1 style={{ fontFamily: "verdana" }}>Login As Student</h1>
            <div className="studentLogin" style={{ backgroundColor: "#3fb1fc" }}>
                <form
                    onSubmit={(event) => {
                        event.preventDefault();
                        console.log(event.target.studentId.value);
                        axios
                            .post("http://localhost:5000/login/student", {
                                username: event.target.studentId.value,
                                password: event.target.password.value,
                            })
                            .then((res) => {
                                console.log("Res", res);
                                navigate("/StudentView/" + event.target.studentId.value);
                            })
                            .catch((err) => {
                                alert("Invalid Credentials");
                                console.log("Err", err);
                            });
                    }}
                >
                    <h3 className="studentLoginH3">Student ID :</h3>
                    <input type="text" name="studentId" />
                    <br />
                    <h3 className="studentLoginH3">Password</h3>
                    <input type="password" name="password" />
                    <br />
                    <button className="studentLoginButton" type="submit">
                        Submit
                    </button>
                </form>
            </div>
        </div>
    )
}

export default StudentLogin;