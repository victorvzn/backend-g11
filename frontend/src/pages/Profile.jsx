import { useEffect, useState } from "react";
import { Header } from "../components/Header";
import styles from "../styles/Profile.module.css";

export const Profile = () => {
  const [profile, setProfile] = useState([]);

  useEffect(() => {
    const getData = async () => {
      const response = await fetch("http://127.0.0.1:5000/perfil", {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      });
      const data = await response.json();
      setProfile(data.data);
    };
    getData();
  }, []);

  return (
    <div className={styles.profile}>
      <Header />
      <div className={styles.profile_content}>
        <div className={styles.wrapper}>
          <div className={styles.profile_card}>
            <div className={styles.profile_card_header}>
              <div className={styles.profile_card_img}>
                <img
                  src={`https://robohash.org/${profile.correo}`}
                  alt="Eduardo De Rivero"
                />
              </div>
            </div>
            <div className={styles.profile_card_body}>
              <h2 className={styles.profile_name}>{profile.nombre}</h2>
              <p className={styles.profile_last_name}>{profile.apellido}</p>
              <div className={styles.profile_buttons}>
                <button>Editar</button>
                <button>Eliminar</button>
                <button>Más</button>
              </div>
              <p className={styles.profile_description}>
                Lorem ipsum dolor sit amet consectetur adipisicing elit.
                Laudantium inventore deleniti voluptas, nobis odit laboriosam
                minima consectetur soluta cupiditate cumque?
              </p>
              {JSON.stringify(profile)}

            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
