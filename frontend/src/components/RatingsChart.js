import React, { useEffect, useState } from "react";
import { Pie } from "react-chartjs-2";
import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement } from "chart.js";

ChartJS.register(Title, Tooltip, Legend, ArcElement);

const backendUrl = "http://127.0.0.1:6001"; // your backend port

function RatingsChart() {
    const [chartData, setChartData] = useState({ labels: [], datasets: [] });

    useEffect(() => {
        fetch(`${backendUrl}/analytics/rating`)  // match backend route
            .then(res => res.json())
            .then(data => {
                if (!data || !data.data) return;

                const labels = data.data.map(item => item.rating);
                const counts = data.data.map(item => item.total_hotels);

                setChartData({
                    labels,
                    datasets: [
                        {
                            label: "Hotel Count per Rating",
                            data: counts,
                            backgroundColor: [
                                "rgba(255, 99, 132, 0.6)",
                                "rgba(54, 162, 235, 0.6)",
                                "rgba(255, 206, 86, 0.6)",
                                "rgba(75, 192, 192, 0.6)",
                                "rgba(153, 102, 255, 0.6)"
                            ]
                        }
                    ]
                });
            })
            .catch(err => console.error("Failed to fetch:", err));
    }, []);

    return (
        <div style={{ width: "100%", maxWidth: "500px", margin: "0 auto", height: "300px" }}>
            <h2>Rating Distribution of Hotels</h2>
            <Pie 
                data={chartData} 
                options={{ responsive: true, maintainAspectRatio: false }} 
                height={250} // smaller pie chart
            />
        </div>
    );
}

export default RatingsChart;