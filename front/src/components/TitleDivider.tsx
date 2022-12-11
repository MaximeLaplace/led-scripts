import React from 'react';

type Props = {
  title: string;
};

export const TitleDivider = ({ title }: Props) => {
  return (
    <>
      <h2>{title}</h2>
      <div
        style={{
          width: '100%',
          height: '1px',
          backgroundColor: '#666666',
          marginBottom: '20px',
          marginTop: '-10px'
        }}
      />
    </>
  );
};
