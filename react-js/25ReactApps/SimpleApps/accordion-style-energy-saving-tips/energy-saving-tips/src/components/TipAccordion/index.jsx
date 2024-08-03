//single selection accordion
//multiple selection accordion
import { useState } from "react";
import tips from "./data";
import "./styles.css";

export default function EnergySavingTips() {
  const [selected, setSelected] = useState(null);

  function handleSingleSelection(getCurrentId) {
    // console.log(getCurrentId);
    setSelected(getCurrentId === selected ? null : getCurrentId);
  }

  console.log(selected);
  return (
    <div className="acc-wrapper">
      <div className="accordion-tip">
        {tips && tips.length > 0 ? (
          tips.map((dataItem) => (
            <div className="item">
              <div
                onClick={() => handleSingleSelection(dataItem.id)}
                className="title"
              >
                <h3>{dataItem.title}</h3>
                <span>+</span>
              </div>
              {selected === dataItem.id ? (
                <div className="acc-content">{dataItem.tip}</div>
              ) : null}
            </div>
          ))
        ) : (
          <div>No data found!</div>
        )}
      </div>
    </div>
  );
}
