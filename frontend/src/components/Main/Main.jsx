import React from 'react';
import PropTypes from 'prop-types';
import { Sidebar } from '../Sidebar/Sidebar';
import { BaseCalendar } from '../BaseCalendar/BaseCalendar';
import styles from './Main.module.css';

export function Main({ localizer }) {
	return (
		<main className={`${styles.main} container`}>
			<Sidebar />
			<div className={styles.content}>
				<BaseCalendar localizer={localizer} />
			</div>
		</main>
	);
}

Main.propTypes = {
	localizer: PropTypes.element.isRequired,
};
