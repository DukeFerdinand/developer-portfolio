import React from "react";
import PropTypes from "prop-types";

import "./Hero.scss";

const Hero = ({ hasImage }) => {
  return <div className="hero-container" />;
};

Hero.propTypes = {
  hasImage: PropTypes.bool
};

export default Hero;
