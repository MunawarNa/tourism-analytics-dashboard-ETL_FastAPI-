import React, { useEffect, useState } from "react";
import { Bar } from "react-chartjs-2";
import { Chart as ChartJS, Title, Tooltip, Legend, CategoryScale, LinearScale, BarElement } from "chart.js";

ChartJS.register(Title, Tooltip, Legend, CategoryScale, LinearScale, BarElement);

const backendUrl = "http://127.0.0.1:6001"; // adjust your backend port

function CitiesChart() {
    const [chartData, setChartData] = useState({ labels: [], datasets: [] });

    useEffect(() => {
        fetch(`${backendUrl}/analytics/cities`)
            .then(res => res.json())
            .then(data => {
                const labels = data.data.map(item => item.city);
                const totalHotels = data.data.map(item => item.total_hotels);
                const avgRatings = data.data.map(item => item.avg_rating);

                setChartData({
                    labels,
                    datasets: [
                        {
                            label: "Total Hotels",
                            data: totalHotels,
                            backgroundColor: "rgba(54, 162, 235, 0.6)",
                        },
                        {
                            label: "Average Rating",
                            data: avgRatings,
                            backgroundColor: "rgba(255, 206, 86, 0.6)",
                        }
                    ]
                });
            });
    }, []);

    return (
        <div>
            <h2>Hotels & Average Ratings per City</h2>
            <Bar data={chartData} options={{ responsive: true }} />
        </div>
    );
}

export default CitiesChart;