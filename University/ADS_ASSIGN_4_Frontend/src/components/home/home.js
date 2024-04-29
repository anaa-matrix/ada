import React from "react";
import Sidebar from "../sidebar/sidebar";
import "./home.css";
function Home() {
  return (
    <div>
      <Sidebar />
      <h1 style={{ textAlign: "center" }}>About us</h1>
      <div className="homeImg">
        <img
          src="https://www.haqseengineer.com/wp-content/uploads/2019/07/1.jpg"
          alt="WCE"
        />
        <p>
          Walchand College of Engineering is situated midway between Sangli and Miraj cities at Vishrambag, Sangli. The WCE campus is located on about 90 acres of land on southern side of Sangli – Miraj road.
          <br />
          In 1947, the college made a modest beginning as New Engineering College, with a single program leading to B.E. (Civil) degree. In the year 1955, the College was renamed as Walchand College of Engineering as part of the new arrangements and pursuant to the Rehabilitation and Development Program mainly funded by Seth Walchand Hirachand Memorial Trust and the Government. The Government appointed an Ad Hoc Committee for conducting the college from May 1955, later replaced by the Administrative Council in 1956. The Ad Hoc Committee added two more degree programs in B.E. (Mechanical) and B.E. (Electrical) in 1955 with the intake of 20 each. Three Diploma programs also started in 1955 – Civil (40 intake), Mechanical (20) and Electrical (20).
          <br />
          Post Graduate programs in Civil, Mechanical and Electrical Engineering and Diploma program in Industrial Electronics were introduced in 1971. In 1986 the UG and PG programs in Electronics Engineering and UG program in Computer Science and Engineering were introduced.
          <br />
          PG program in CSE was introduced in 1997. In 2001, added B.E. program in Information Technology with an intake of 60 students. An additional intake of 30 students was also sanctioned for Computer Science & Engineering program, resulting in total intake of 390 students for all branches at UG level and 106 at PG level. As part of strategic planning, PG section is being strengthened and PG intake has now steadily risen to 240 across 10 programs. The College has a QIP scheme for full-time doctoral programs and also offers Ph. D. programs of Shivaji University in various branches of engineering.
        </p>
      </div>
    </div>
  );
}

export default Home;
