import React from "react";
import CitiesChart from "./components/CitiesChart";
import RatingsChart from "./components/RatingsChart";
// import TopCitiesChart from "./components/TopCitiesChart"; // optional third chart
import "./App.css";

function App() {
    return (
        <div style={{ padding: "20px" }}>
            <h1 style={{ textAlign: "center" }}>Tourism Analytics Dashboard in France</h1>

            {/* Chart container */}
            <div style={{
                display: "flex",
                flexWrap: "wrap",   // wraps charts on smaller screens
                justifyContent: "space-around",
                gap: "20px",
                marginTop: "30px"
            }}>
                <div style={{ flex: "1 1 400px", minWidth: "300px" }}>
                    <CitiesChart />
                </div>
                <div style={{ flex: "1 1 400px", minWidth: "300px" }}>
                    <RatingsChart />
                </div>
                {/* <div style={{ flex: "1 1 400px", minWidth: "300px" }}>
                    <TopCitiesChart />
                </div> */}
            </div>
        </div>
    );
}

export default App;