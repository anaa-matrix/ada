const express = require("express");
const cors = require("cors");
const mysql = require("mysql");
const emailjs = require("emailjs-com");

const app = express();
const port = 5000;

app.use(express.json());
app.use(cors());

// MySQL database connection configuration
const connection = mysql.createConnection({
    host: 'localhost',
    user: 'Eass1',
    password: '#@$Mysql1.',
    database: 'contactform',
  });

connection.connect((err) => {
  if (err) {
    console.error("Error connecting to MySQL:", err);
    return;
  }
  console.log("Connected to MySQL database!");
});

// Endpoint to handle sending emails and saving data to MySQL
app.post("/sendEmail", (req, res) => {
  const { user_name, email, message } = req.body;

  // Send email using emailjs
  emailjs
    .send(
      "YOUR_SERVICE_ID",
      "YOUR_TEMPLATE_ID",
      {
        to_name: "Recipient Name",
        from_name: user_name,
        message: message,
        reply_to: email,
      },
      "YOUR_USER_ID"
    )
    .then(
      (response) => {
        console.log("Email sent:", response);
        
        // Insert data into MySQL after sending email
        const sql = "INSERT INTO messages (user_name, email, message) VALUES (?, ?, ?)";
        connection.query(sql, [user_name, email, message], (error, results) => {
          if (error) {
            console.error("Error inserting data into MySQL:", error);
            res.status(500).json({ success: false, error: error });
          } else {
            console.log("Data inserted into MySQL successfully");
            res.status(200).json({ success: true });
          }
        });
      },
      (error) => {
        console.error("Email send error:", error);
        res.status(500).json({ success: false, error: error });
      }
    );
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
