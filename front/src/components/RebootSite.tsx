import React from 'react';
import axios from 'axios';

import { Button, Grid } from '@mui/material';

import { useRebootDialog } from './ConfirmationDialog';
import { TitleDivider } from './TitleDivider';

export const RebootSite = () => {
	const rebootSite = (password: string) => () => {
		console.log('yolo');
		axios({
			url: '/reboot_site',
			method: 'POST',
			data: {
				password
			}
		});
	};

	const { ConfirmationDialog, handleOpen } = useRebootDialog(rebootSite);

	return (
		<>
			<TitleDivider title="Reboot site" />
			<Grid container spacing={4} justifyContent="center">
				<Grid item xs={8} sm={3}>
					<Button variant="contained" fullWidth onClick={handleOpen}>
						Reboot site
					</Button>
				</Grid>
				<ConfirmationDialog />
			</Grid>
		</>
	);
};
