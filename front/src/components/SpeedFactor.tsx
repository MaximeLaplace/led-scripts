import React, { useEffect, useState } from 'react';
import axios from 'axios';

import {
	Button,
	createTheme,
	Grid,
	TextField,
	ThemeProvider
} from '@mui/material';

import { TitleDivider } from './TitleDivider';

const darkTheme = createTheme({
	palette: {
		mode: 'dark'
	}
});

export const SpeedFactor = () => {
	const [speedFactor, setSpeedFactor] = useState<string | null>(null);

	useEffect(() => {
		const get = async () => {
			const { data } = await axios({
				url: '/speed_factor',
				method: 'GET'
			});
			setSpeedFactor(data);
		};
		get();
	}, []);

	const handleChange = (
		event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
	) => {
		setSpeedFactor(event.currentTarget.value);
	};

	const handleSubmit = () => {
		if (
			speedFactor !== null &&
			parseFloat(speedFactor).toString() === speedFactor
		) {
			axios({
				url: `/speed_factor/${speedFactor}`,
				method: 'POST'
			});
		}
	};

	return (
		<>
			<ThemeProvider theme={darkTheme}>
				<TitleDivider title="Speed Factor" />
				<Grid container justifyContent="center" sx={{ marginBottom: '20px' }}>
					{speedFactor !== null ? (
						<Grid item justifyContent="center">
							<div>
								<TextField
									label="Speed factor"
									id="outlined-size-small"
									defaultValue={speedFactor}
									size="small"
									onChange={handleChange}
									sx={{
										marginRight: '20px'
									}}
								/>
								<Button variant="contained" onClick={handleSubmit}>
									GO
								</Button>
							</div>
						</Grid>
					) : (
						<Grid item>Loading speed factor...</Grid>
					)}
				</Grid>
			</ThemeProvider>
		</>
	);
};
