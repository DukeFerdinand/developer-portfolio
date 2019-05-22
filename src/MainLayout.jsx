import React, { Fragment } from "react";
import { Route, Switch, BrowserRouter as Router } from "react-router-dom";

import Index from "./routes/Index";
import NotFound from "./routes/NotFound";

const MainLayout = () => {
  return (
    <Router>
      <Fragment>
        {/* Header */}
        {/* Main Layout */}
        <Switch>
          <Route path="/" exact component={Index} />
          <Route component={NotFound} />
        </Switch>
        {/* Footer */}
      </Fragment>
    </Router>
  );
};

export default MainLayout;
